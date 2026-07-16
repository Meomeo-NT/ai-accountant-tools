#!/usr/bin/env python3
"""HERMES BDS Receiver API — FastAPI on port 8082"""
from dotenv import load_dotenv
load_dotenv('/root/bds-crawler/.env')

from fastapi import FastAPI, Header, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
import sqlite3, os, asyncio, httpx, json, random
from datetime import datetime
from contextlib import contextmanager

app = FastAPI(title="HERMES BDS Receiver", version="2.0")

DB_PATH = "/root/bds-crawler/data/bds_data.db"
RECEIVER_SECRET = os.getenv("RECEIVER_SECRET", "hermes_bds_default_key")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "1155632924")
HERMES_CHAT_ID = os.getenv("HERMES_CHAT_ID", "")

class ListingItem(BaseModel):
    url: str
    title: Optional[str] = None
    price: Optional[float] = None
    area: Optional[float] = None
    district: Optional[str] = None
    ward: Optional[str] = None
    listing_type: Optional[str] = "ban"
    source: str
    raw_text: Optional[str] = None

class CrawlBatch(BaseModel):
    listings: List[ListingItem]
    run_id: str
    source: str
    total_crawled: int

@contextmanager
def db_conn():
    conn = sqlite3.connect(DB_PATH, timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    try:
        yield conn
    finally:
        conn.close()

def compute_price_m2(price, area):
    if price and area and area > 0:
        return round(price / area, 2)
    return None

def generate_title_hint(listing, price_m2, diff_pct):
    district_map = {
        "nha-trang": "Nha Trang", "cam-ranh": "Cam Ranh",
        "ninh-hoa": "Ninh Hoa", "van-ninh": "Van Ninh",
    }
    d_name = district_map.get(listing.district, listing.district or "Khanh Hoa")
    templates = [
        f"Cat lo sau {diff_pct:.0f}% — BDS {d_name} re hon thi truong {diff_pct:.0f}%",
        f"Co hoi hiem: {d_name} chi {price_m2:.0f}tr/m2, thap hon khu vuc {diff_pct:.0f}%",
        f"Thanh ly gap BDS {d_name} — gia {price_m2:.0f}tr/m2, re hon TB {diff_pct:.0f}%",
    ]
    return random.choice(templates)

async def check_hot_and_notify(listing_id, listing, price_m2):
    if not price_m2 or not listing.district:
        return
    with db_conn() as conn:
        row = conn.execute("""
            SELECT ma30 FROM price_stats
            WHERE district = ? AND listing_type = ?
            ORDER BY date DESC LIMIT 1
        """, (listing.district, listing.listing_type or "ban")).fetchone()
        if not row or not row["ma30"]:
            return
        ma30 = row["ma30"]
        diff_pct = (ma30 - price_m2) / ma30 * 100
        if diff_pct >= 12:
            hot_reason = f"Thap hon MA30 {diff_pct:.1f}% (MA30={ma30:.0f}tr/m2)"
            conn.execute("UPDATE listings SET is_hot=1, hot_reason=? WHERE id=?", (hot_reason, listing_id))
            conn.commit()
            await send_hot_alert(listing, price_m2, diff_pct, hot_reason)

async def send_hot_alert(listing, price_m2, diff_pct, reason):
    if not TELEGRAM_BOT_TOKEN:
        return
    emoji = "🔥🔥" if diff_pct >= 18 else "🔥"
    msg = f"{emoji} *BDS SIÊU HOT — {listing.district}*\n\n📌 {listing.title or 'Khong ro tieu de'}\n💰 Gia: {listing.price:.0f} trieu | {price_m2:.0f}tr/m2\n📉 {reason}\n🔗 {listing.url}"
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            await client.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
            )
    except:
        pass

@app.post("/ingest")
async def ingest_batch(batch: CrawlBatch, background_tasks: BackgroundTasks, x_secret: str = Header(None)):
    if x_secret != RECEIVER_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")
    with db_conn() as conn:
        new_count = 0
        hot_checks = []
        for item in batch.listings:
            seen = conn.execute("SELECT 1 FROM seen_urls WHERE url=?", (item.url,)).fetchone()
            if seen:
                continue
            price_m2 = compute_price_m2(item.price, item.area)
            now = datetime.now().isoformat()
            cur = conn.execute("""
                INSERT OR IGNORE INTO listings
                (url, title, price, area, price_m2, district, ward, listing_type, source, raw_text, created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """, (item.url, item.title, item.price, item.area, price_m2,
                  item.district, item.ward, item.listing_type, item.source,
                  item.raw_text, now))
            conn.execute("INSERT OR IGNORE INTO seen_urls(url, source, seen_at) VALUES(?,?,?)", (item.url, item.source, now))
            if cur.lastrowid and price_m2:
                hot_checks.append((cur.lastrowid, item, price_m2))
            new_count += 1
        conn.commit()
    for listing_id, item, pm2 in hot_checks:
        background_tasks.add_task(check_hot_and_notify, listing_id, item, pm2)
    return {"status": "ok", "new": new_count, "total_in_batch": len(batch.listings), "run_id": batch.run_id}

@app.post("/update-stats")
async def update_price_stats(x_secret: str = Header(None)):
    if x_secret != RECEIVER_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")
    with db_conn() as conn:
        today = datetime.now().strftime("%Y-%m-%d")
        updated = 0
        districts = conn.execute("SELECT DISTINCT district, listing_type FROM listings WHERE district IS NOT NULL").fetchall()
        for row in districts:
            district, ltype = row["district"], row["listing_type"]
            stats = conn.execute("""
                SELECT AVG(price_m2) as avg_pm2, COUNT(*) as cnt
                FROM listings WHERE district=? AND listing_type=? AND price_m2 IS NOT NULL AND price_m2 > 0
                AND created_at >= date('now','-30 days')
            """, (district, ltype)).fetchone()
            if stats and stats["avg_pm2"] and stats["cnt"] >= 3:
                conn.execute("""
                    INSERT OR REPLACE INTO price_stats(district, listing_type, date, avg_price_m2, ma30, sample_count)
                    VALUES(?,?,?,?,?,?)
                """, (district, ltype, today, stats["avg_pm2"], stats["avg_pm2"], stats["cnt"]))
                updated += 1
        conn.commit()
    return {"status": "ok", "stats_updated": updated, "date": today}

@app.get("/health")
async def health():
    with db_conn() as conn:
        total = conn.execute("SELECT COUNT(*) as n FROM listings").fetchone()["n"]
        hot = conn.execute("SELECT COUNT(*) as n FROM listings WHERE is_hot=1").fetchone()["n"]
    return {"status": "ok", "total_listings": total, "hot_listings": hot}

@app.get("/hot")
async def get_hot_listings(limit: int = 20, x_secret: str = Header(None)):
    if x_secret != RECEIVER_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")
    with db_conn() as conn:
        rows = conn.execute("""
            SELECT title, price, area, price_m2, district, hot_reason, url, created_at
            FROM listings WHERE is_hot=1 ORDER BY created_at DESC LIMIT ?
        """, (limit,)).fetchall()
    return [dict(r) for r in rows]

@app.get("/stats")
async def get_stats(x_secret: str = Header(None)):
    if x_secret != RECEIVER_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")
    with db_conn() as conn:
        by_source = conn.execute("SELECT source, count(*) as cnt FROM listings GROUP BY source").fetchall()
        by_district = conn.execute("SELECT district, count(*) as cnt FROM listings WHERE district IS NOT NULL GROUP BY district ORDER BY cnt DESC LIMIT 10").fetchall()
        recent = conn.execute("SELECT count(*) as n FROM listings WHERE created_at >= date('now','-1 day')").fetchone()["n"]
    return {
        "by_source": [dict(r) for r in by_source],
        "by_district": [dict(r) for r in by_district],
        "recent_24h": recent,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)