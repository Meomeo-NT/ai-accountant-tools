#!/usr/bin/env python3
"""BDS Phase 2 — Create SQLite database and migrate seen.json"""
import sqlite3, json, os, shutil
from datetime import datetime

DB_PATH = "/root/bds-crawler/data/bds_data.db"
SEEN_JSON = "/root/bds-crawler/data/seen.json"

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Bảng Listings
c.executescript("""
CREATE TABLE IF NOT EXISTS listings (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    url         TEXT UNIQUE NOT NULL,
    title       TEXT,
    price       REAL,
    area        REAL,
    price_m2    REAL,
    district    TEXT,
    ward        TEXT,
    listing_type TEXT,
    source      TEXT,
    raw_text    TEXT,
    created_at  TEXT NOT NULL,
    is_hot      INTEGER DEFAULT 0,
    hot_reason  TEXT,
    notified    INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS seen_urls (
    url         TEXT PRIMARY KEY,
    source      TEXT,
    seen_at     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS price_stats (
    district    TEXT NOT NULL,
    listing_type TEXT NOT NULL,
    date        TEXT NOT NULL,
    avg_price_m2 REAL,
    ma30        REAL,
    sample_count INTEGER,
    PRIMARY KEY (district, listing_type, date)
);

CREATE INDEX IF NOT EXISTS idx_listings_district ON listings(district);
CREATE INDEX IF NOT EXISTS idx_listings_created ON listings(created_at);
CREATE INDEX IF NOT EXISTS idx_listings_hot ON listings(is_hot);
""")

# Migrate seen.json -> seen_urls (sử dụng shutil.copy thay vì rename)
migrated = 0
if os.path.exists(SEEN_JSON):
    try:
        with open(SEEN_JSON) as f:
            seen_data = json.load(f)
        if isinstance(seen_data, list):
            urls = seen_data
        elif isinstance(seen_data, dict):
            urls = list(seen_data.keys())
        else:
            urls = []
        now = datetime.now().isoformat()
        c.executemany(
            "INSERT OR IGNORE INTO seen_urls(url, source, seen_at) VALUES(?,?,?)",
            [(u, "legacy", now) for u in urls]
        )
        migrated = len(urls)
        shutil.copy(SEEN_JSON, SEEN_JSON + ".bak")
        print(f"✅ Migrated {migrated} URLs -> SQLite")
        print(f"✅ Backup: seen.json.bak (file gốc GIỮ NGUYÊN cho Phase 1)")
    except Exception as e:
        print(f"⚠️ Migrate lỗi (an toàn): {e}")

# Also migrate data from all.json if exists
DATA_DIR = "/root/bds-crawler/data"
ALLJSON = os.path.join(DATA_DIR, "all.json")
if os.path.exists(ALLJSON):
    try:
        with open(ALLJSON, encoding='utf-8') as f:
            all_items = json.load(f)
        print(f"📦 Found {len(all_items)} items in all.json")
        for item in all_items:
            url = item.get("url", "")
            if not url:
                continue
            seen = c.execute("SELECT 1 FROM seen_urls WHERE url=?", (url,)).fetchone()
            if seen:
                continue
            try:
                pm2 = None
                price = item.get("price_num")
                area = item.get("area_num")
                if price and area and area > 0:
                    pm2 = round(price / area, 2)
                c.execute("""
                    INSERT OR IGNORE INTO listings
                    (url, title, price, area, price_m2, district, listing_type, source, raw_text, created_at)
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                """, (
                    url,
                    item.get("title"),
                    price/1e6 if price and price > 1e6 else price,  # Convert to triệu
                    area,
                    pm2,
                    item.get("address", ""),
                    "ban",
                    "alonhadat",
                    item.get("brief", ""),
                    item.get("crawl_date", datetime.now().isoformat())
                ))
                c.execute(
                    "INSERT OR IGNORE INTO seen_urls(url, source, seen_at) VALUES(?,?,?)",
                    (url, "alonhadat", datetime.now().isoformat())
                )
            except Exception:
                continue
        conn.commit()
        print(f"✅ {len(all_items)} items from all.json migrated to SQLite")
    except Exception as e:
        print(f"⚠️ all.json migrate error: {e}")

conn.commit()
conn.close()
print(f"✅ Database created at: {DB_PATH}")