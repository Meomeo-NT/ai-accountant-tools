#!/usr/bin/env python3
"""
BDS Crawler v3: Google Sheets + Telegram + File Log
"""
import json, requests, re, os
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

load_dotenv('/root/bds-crawler/.env')

# CONFIG
PAGES = 5
USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)"
BASE_URL = "https://alonhadat.com.vn/can-ban-nha-dat/khanh-hoa"

SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
SERVICE_ACCOUNT_FILE = "/root/bds-crawler/service-account-key.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT = os.getenv("TELEGRAM_CHAT_ID")
ZALO_NOTIFY_URL = os.getenv("ZALO_NOTIFY_URL", "http://localhost:8081/notify")

DATA_DIR = "data"
SEEN_FILE = f"{DATA_DIR}/seen.json"
NOTIF_FILE = f"{DATA_DIR}/notifications.json"
os.makedirs(DATA_DIR, exist_ok=True)

# GOOGLE SHEETS
def setup_google_sheets():
    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = gspread.authorize(creds)
        return client.open_by_key(SHEET_ID).sheet1
    except Exception as e:
        print(f"Google Sheets: {e}")
        return None

# DATA
def load_seen():
    if os.path.exists(SEEN_FILE):
        try:
            with open(SEEN_FILE) as f:
                return set(json.load(f))
        except:
            pass
    return set()

def save_seen(seen_set):
    with open(SEEN_FILE, "w") as f:
        json.dump(sorted(list(seen_set)), f)

def extract_ma_tin(url):
    m = re.search(r'-(\d+)\.html', url)
    return m.group(1) if m else None

# CRAWL
def crawl_page(page):
    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/trang-{page}"
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=10)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.find_all("article", class_="property-item")
        results = []
        for item in items:
            try:
                title = item.find("h3", class_="property-title")
                link = item.find("a", class_="link")
                price = item.find("span", class_="price")
                area = item.find("span", class_="area")
                addr = item.find("p", class_="new-address")
                img = item.find("img")
                if not link:
                    continue
                url_tin = "https://alonhadat.com.vn" + link["href"]
                ma_tin_m = extract_ma_tin(url_tin)
                if not ma_tin_m:
                    continue
                price_text = ""
                if price:
                    inner_price = price.find("span", class_="value")
                    price_text = inner_price.get_text(strip=True) if inner_price else price.get_text(strip=True).replace("Gi\u00e1:", "").strip()
                area_text = ""
                if area:
                    inner_area = area.find("span", class_="value")
                    area_text = inner_area.get_text(strip=True) if inner_area else area.get_text(strip=True).replace("Di\u1ec7n t\u00edch:", "").strip()
                addr_text = addr.get_text(strip=True) if addr else ""
                results.append({
                    "ma_tin": ma_tin_m,
                    "title": title.get_text(strip=True) if title else "N/A",
                    "price": price_text if price_text else "N/A",
                    "area": area_text if area_text else "N/A",
                    "address": addr_text if addr_text else "N/A",
                    "url": url_tin,
                    "image": img.get("src", "") if img else "",
                    "crawl_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            except:
                pass
        print(f"Page {page}: {len(results)} items")
        return results
    except Exception as e:
        print(f"Page {page} error: {e}")
        return []

# SAVE TO SHEETS
def save_to_google_sheets(sheet, new_items):
    if not sheet or not new_items:
        return 0
    try:
        rows = []
        now = datetime.now().strftime("%Y-%m-%d")
        for item in new_items:
            rows.append([
                item["crawl_date"], item["ma_tin"], item["title"],
                item["price"], item["area"], item["address"],
                item["url"], item["image"], "BDS", now
            ])
        sheet.append_rows(rows)
        print(f"Google Sheets: {len(rows)} rows")
        return len(rows)
    except Exception as e:
        print(f"Sheets save error: {e}")
        return 0

# TELEGRAM
def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT:
        print("Telegram config missing")
        return False
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        resp = requests.post(url, json={
            "chat_id": TELEGRAM_CHAT,
            "text": message,
            "parse_mode": "HTML"
        }, timeout=5)
        if resp.status_code == 200:
            print("Telegram sent")
            return True
        print(f"Telegram status: {resp.status_code}")
    except Exception as e:
        print(f"Telegram error: {e}")
    return False

# FILE LOG
def save_notification(message):
    try:
        notif = {"timestamp": datetime.now().isoformat(), "message": message}
        if os.path.exists(NOTIF_FILE):
            with open(NOTIF_FILE) as f:
                history = json.load(f)
        else:
            history = []
        history.append(notif)
        with open(NOTIF_FILE, "w") as f:
            json.dump(history[-100:], f)
        return True
    except Exception as e:
        print(f"Save notif error: {e}")
        return False

# NOTIFY
def notify_crawl_done(new_count):
    status = "OK" if new_count > 0 else "No new"
    message = f"Crawl BDS xong! Tim {new_count} tin moi ({datetime.now().strftime('%H:%M %d/%m')})"
    send_telegram(message)
    save_notification(message)
    try:
        requests.post(ZALO_NOTIFY_URL, json={"message": message}, timeout=3)
    except:
        pass

# MAIN
def main():
    print(f"Start crawl: {datetime.now()}")
    sheet = setup_google_sheets()
    seen = load_seen()
    all_items = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(crawl_page, p): p for p in range(1, PAGES + 1)}
        for future in as_completed(futures):
            try:
                all_items.extend(future.result())
            except Exception as e:
                print(f"Error: {e}")

    new_items = [x for x in all_items if x["ma_tin"] not in seen]
    for item in new_items:
        seen.add(item["ma_tin"])

    print(f"Total: {len(all_items)}, New: {len(new_items)}")
    if new_items and sheet:
        save_to_google_sheets(sheet, new_items)
    notify_crawl_done(len(new_items))
    save_seen(seen)
    print(f"Done! DB: {len(seen)}")

if __name__ == "__main__":
    main()