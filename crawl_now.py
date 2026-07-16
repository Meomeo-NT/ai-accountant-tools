"""
crawl_now.py — Script crawl toàn bộ hệ thống XHTDVRB thực tế
Chạy: python crawl_now.py
"""

import os, sys, hashlib, json, time, logging, re
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse
from collections import deque

# Fix encoding cho Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# ── Cấu hình ──────────────────────────────────────────────
BASE_URL = os.getenv("BASE_URL", "http://10.62.2.41:8080/XHTDVRB")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LANGUAGE = os.getenv("LANGUAGE", "2")

PROJECT = Path(__file__).parent.absolute()
RAW_HTML = PROJECT / "raw" / "html";  RAW_HTML.mkdir(parents=True, exist_ok=True)
RAW_JS   = PROJECT / "raw" / "js";    RAW_JS.mkdir(parents=True, exist_ok=True)
RAW_API  = PROJECT / "raw" / "api";   RAW_API.mkdir(parents=True, exist_ok=True)
ANALYSIS = PROJECT / "analysis";      ANALYSIS.mkdir(parents=True, exist_ok=True)
LOGS     = PROJECT / "logs";          LOGS.mkdir(parents=True, exist_ok=True)

log_file = LOGS / f"crawl_{datetime.now():%Y%m%d_%H%M%S}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(str(log_file), encoding="utf-8"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9",
})

# ── Kết quả tổng hợp ──────────────────────────────────────
RESULT = {
    "login_success": False,
    "pages_crawled": [],
    "forms": [],
    "selects": {},
    "tables": [],
    "js_findings": [],
    "api_responses": {},
    "score_submit": [],
    "weights_found": {},
}

# ══════════════════════════════════════════════════════════
# 1. ĐĂNG NHẬP
# ══════════════════════════════════════════════════════════
def hash_password(raw_pass: str, username: str) -> str:
    return hashlib.md5(f"{raw_pass}_{username}".encode()).hexdigest()

def dang_nhap() -> bool:
    log.info("🔐 Đang đăng nhập...")
    print("\n🔐 Đang đăng nhập...")

    try:
        r = session.get(BASE_URL + "/", timeout=15)
        r.raise_for_status()
    except Exception as e:
        log.error(f"❌ Không kết nối được: {e}")
        return False

    # Lưu HTML login
    (RAW_HTML / "login.html").write_text(r.text, encoding="utf-8")

    soup = BeautifulSoup(r.text, "lxml")

    # Tìm form login
    form = soup.find("form", id=lambda x: x and "login" in x.lower()) or soup.find("form")
    if not form:
        log.error("❌ Không tìm thấy form đăng nhập!")
        return False

    # Lấy action URL — dùng BASE_URL làm base (có context /XHTDVRB)
    # QUAN TRỌNG: Phải GIỮ NGUYÊN jsessionid vì server Struts yêu cầu nó trong URL
    action = form.get("action", "")
    if not action.startswith("http"):
        action = urljoin(BASE_URL.rstrip("/") + "/", action)
    log.info(f"   Form action: {action}")

    hash_pass = hash_password(PASSWORD, USERNAME)
    log.info(f"   Hash mật khẩu: {hash_pass[:16]}...")

    # POST với các field cần thiết
    data = {
        "userName": USERNAME,
        "password": hash_pass,
        "language": LANGUAGE,
    }

    try:
        r2 = session.post(action, data=data, timeout=15, allow_redirects=True)
        log.info(f"   POST login: status={r2.status_code}, url cuối={r2.url}")
    except Exception as e:
        log.error(f"❌ Lỗi POST login: {e}")
        return False

    # Kiểm tra thành công — nếu còn form login thì thất bại
    final_soup = BeautifulSoup(r2.text, "lxml")
    still_login = final_soup.find("form", id=lambda x: x and "login" in x.lower())
    
    # Debug: in 200 ký tự đầu response
    debug_text = r2.text[:200].replace("\n", " ").strip()
    log.info(f"   Response snippet: {debug_text}")

    if still_login or "login" in r2.url.lower():
        # Tìm thông báo lỗi
        error_elem = final_soup.find(string=lambda t: t and ("sai" in t.lower() or "error" in t.lower() or "fail" in t.lower()))
        if error_elem:
            log.error(f"❌ Lỗi đăng nhập: {error_elem}")
        # In mấy dòng đầu response
        log.error(f"❌ Đăng nhập thất bại — vẫn ở trang login!")
        log.error(f"   URL hiện tại: {r2.url}")
        return False

    log.info("✅ Đăng nhập thành công!")
    RESULT["login_success"] = True

    # Lưu trang chủ
    (RAW_HTML / "main.html").write_text(r2.text, encoding="utf-8")
    RESULT["pages_crawled"].append(r2.url)

    return True

# ══════════════════════════════════════════════════════════
# 2. CRAWL BFS
# ══════════════════════════════════════════════════════════
PRIORITY_KEYWORDS = [
    "khdn", "khcn", "canhan", "ca-nhan", "doanhghiep", "doanh-nghiep",
    "tieuchi", "chiso", "xeploai", "xep-loai", "chitiet", "chi-tiet",
    "nhom", "phanloai", "phan-loai", "nhaplieu", "nhap-lieu",
    "form", "scoring", "rating", "config", "setup", "input", "data",
    "cham", "diem", "hang", "loai", "kh", "index", "home", "main"
]

def is_internal(url: str) -> bool:
    return "XHTDVRB" in url or "/XHTDVRB" in url

def normalize_url(url: str, base: str) -> str:
    if not url or url.startswith("#") or url.startswith("javascript"):
        return ""
    if url.startswith("//"):
        return "http:" + url
    if url.startswith("/"):
        # Nếu URL đã có context path XHTDVRB, dùng trực tiếp
        if url.startswith("/XHTDVRB"):
            parsed = urlparse(BASE_URL)
            return f"{parsed.scheme}://{parsed.netloc}{url}"
        else:
            # Thêm context path /XHTDVRB
            return BASE_URL.rstrip("/") + url
    # Relative path: thêm context path
    if not url.startswith("http"):
        # Nếu là relative (vd: "login;jsessionid=..."), prepend BASE_URL path
        if ";" in url or "/" not in url:
            return BASE_URL.rstrip("/") + "/" + url.split(";")[0]
        return urljoin(base, url)
    return url

def crawl_tat_ca():
    visited = set()
    queue = deque()

    # Thêm URL gốc
    queue.append(BASE_URL + "/")

    # Thêm URL ưu tiên
    for kw in PRIORITY_KEYWORDS:
        for suffix in [f"/{kw}", f"/{kw}.action", f"/{kw}.do"]:
            queue.appendleft(BASE_URL + suffix)

    count = 0
    while queue and count < 200:  # Giới hạn 200 URL
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            log.info(f"📄 [{count+1}] Crawling: {url}")
            r = session.get(url, timeout=15)

            if r.status_code != 200:
                log.warning(f"  → Status {r.status_code}")
                continue

            ct = r.headers.get("content-type", "").lower()

            # Lưu JS
            if "javascript" in ct:
                slug = url.replace(BASE_URL, "").strip("/").replace("/", "_").replace("?", "_") or "main"
                fpath = RAW_JS / f"{slug}.js"
                fpath.write_text(r.text, encoding="utf-8")
                phan_tich_js(r.text, str(fpath))
                continue

            # Lưu JSON API
            if "json" in ct:
                slug = url.replace(BASE_URL, "").strip("/").replace("/", "_").replace("?", "_") or "api"
                fpath = RAW_API / f"{slug}.json"
                fpath.write_text(r.text, encoding="utf-8")
                RESULT["api_responses"][url] = r.text[:500]
                log.info(f"  → JSON API ({len(r.text)} chars)")
                continue

            if "html" not in ct and "text" not in ct:
                continue

            # Lưu HTML
            slug = url.replace(BASE_URL, "").strip("/").replace("/", "_").replace("?", "_") or "index"
            fpath = RAW_HTML / f"{slug}.html"
            fpath.write_text(r.text, encoding="utf-8")
            RESULT["pages_crawled"].append(url)
            count += 1

            soup = BeautifulSoup(r.text, "lxml")

            # Parse HTML components
            phan_tich_form(soup, url)
            phan_tich_select(soup, url)
            phan_tich_table(soup, url)
            tim_trong_so(soup, url)

            # Tải JS files
            for script in soup.find_all("script", src=True):
                js_url = normalize_url(script["src"], url)
                if js_url and is_internal(js_url) and js_url not in visited:
                    queue.appendleft(js_url)

            # Tìm links
            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                full = normalize_url(href, url)
                if full and is_internal(full) and full not in visited:
                    if any(kw in full.lower() for kw in PRIORITY_KEYWORDS):
                        queue.appendleft(full)
                    else:
                        queue.append(full)

            time.sleep(0.2)

        except Exception as e:
            log.error(f"  → Lỗi: {e}")

    log.info(f"\n✅ Đã crawl xong {count} trang HTML")

# ══════════════════════════════════════════════════════════
# 3. PARSE CHI TIẾT
# ══════════════════════════════════════════════════════════
def phan_tich_form(soup: BeautifulSoup, url: str):
    for form in soup.find_all("form"):
        action = form.get("action", "")
        if not action.startswith("http"):
            action = urljoin(url, action)
        method = form.get("method", "GET").upper()

        fields = []
        for inp in form.find_all(["input", "select", "textarea"]):
            name = inp.get("name") or inp.get("id") or ""
            typ = inp.get("type", inp.name)
            opts = []

            if inp.name == "select":
                for opt in inp.find_all("option"):
                    v = opt.get("value", "")
                    t = opt.get_text(strip=True)
                    if v or t:
                        opts.append({"value": v, "text": t})

            if name:
                fields.append({"name": name, "type": typ, "options": opts})

        if fields:
            RESULT["forms"].append({
                "url": url, "action": action, "method": method, "fields": fields
            })
            log.info(f"  📋 Form: {action} [{method}] — {len(fields)} fields")
            for f in fields:
                if f["options"]:
                    log.info(f"    SELECT [{f['name']}]: {len(f['options'])} options")

def phan_tich_select(soup: BeautifulSoup, url: str):
    for sel in soup.find_all("select"):
        name = sel.get("name") or sel.get("id") or "unknown"
        opts = []
        for opt in sel.find_all("option"):
            v = opt.get("value", "")
            t = opt.get_text(strip=True)
            if v or t:
                opts.append({"value": v, "text": t})
        if opts:
            RESULT["selects"][f"{url}#{name}"] = opts
            # In chi tiết nếu có ít option
            if len(opts) <= 20:
                for o in opts:
                    log.info(f"    SELECT [{name}]: {o['value']:10s} → {o['text']}")

def phan_tich_table(soup: BeautifulSoup, url: str):
    for tbl in soup.find_all("table"):
        rows = tbl.find_all("tr")
        if len(rows) < 2:
            continue
        headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
        data_rows = []
        for row in rows[1:]:
            cells = [td.get_text(strip=True) for td in row.find_all("td")]
            if cells:
                data_rows.append(cells)
        if headers:
            RESULT["tables"].append({"url": url, "headers": headers, "rows": data_rows})
            log.info(f"  📊 Table: {headers} ({len(data_rows)} rows)")
            for row in data_rows[:5]:
                log.info(f"    {row}")

def tim_trong_so(soup: BeautifulSoup, url: str):
    """Tìm trọng số, điểm, % trong text"""
    text = soup.get_text()
    patterns = [
        (r'(\d+\.?\d*)\s*%', 'percent'),
        (r'(trọng số|trongso|he so|hệ số|weight)\s*[:=]\s*(\d+\.?\d*)', 'weight'),
        (r'(điểm|diem|score)\s*[:=]\s*(\d+\.?\d*)', 'score'),
        (r'(hạng|hang|rank|xep loại|xếp loại)\s*[:=]?\s*(\w+)', 'rank'),
    ]
    for pat, label in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            key = f"{url}:{label}"
            if key not in RESULT["weights_found"]:
                RESULT["weights_found"][key] = []
            RESULT["weights_found"][key].append(m.groups())
            log.info(f"  🔢 {label}: {m.groups()}")

def phan_tich_js(js_text: str, filepath: str):
    import re
    keywords = [
        "weight", "trongso", "heso", "diem", "score", "rank", "xephang",
        "nguong", "threshold", "phanloai", "nhom", "criteria", "tieuchi",
        "loaiKH", "loai_kh", "doanhNghiep", "caNhan"
    ]
    lines = js_text.split("\n")
    for i, line in enumerate(lines):
        if any(kw in line.lower() for kw in keywords):
            ctx = "\n".join(lines[max(0,i-3):i+4])
            RESULT["js_findings"].append({
                "file": filepath,
                "line": i+1,
                "content": ctx.strip()
            })
            log.info(f"  🔍 JS [{Path(filepath).name}:{i+1}]: {line.strip()[:120]}")

    # Tìm URL API trong JS
    for m in re.finditer(r'["\'](/XHTDVRB/[^"\'?\s]+)["\']', js_text):
        api_url = "http://10.62.2.41:8080" + m.group(1)
        if api_url not in RESULT["api_responses"] and api_url not in [x for x in RESULT["api_responses"]]:
            try:
                log.info(f"  🌐 API từ JS: {api_url}")
                r = session.get(api_url, timeout=10)
                slug = m.group(1).strip("/").replace("/", "_")
                fpath = RAW_API / f"js_{slug}.txt"
                fpath.write_text(r.text[:5000], encoding="utf-8")
                RESULT["api_responses"][api_url] = r.text[:300]
                log.info(f"    → {r.status_code} ({len(r.text)} chars)")
            except:
                pass

# ══════════════════════════════════════════════════════════
# 4. THỬ SUBMIT FORM CHẤM ĐIỂM
# ══════════════════════════════════════════════════════════
def thu_submit_form():
    log.info("\n📝 Thử submit form chấm điểm...")
    for form_info in RESULT["forms"]:
        action = form_info["action"].lower()
        keywords = ["score", "diem", "xep", "tinh", "kh", "input", "nhap", "cham"]
        if not any(kw in action for kw in keywords):
            continue

        test_data = {}
        for field in form_info["fields"]:
            name = field["name"]
            if field["options"]:
                for opt in field["options"]:
                    if opt["value"]:
                        test_data[name] = opt["value"]
                        break
            elif field["type"] in ["text", "number"]:
                test_data[name] = "1"

        if test_data:
            try:
                log.info(f"  POST {form_info['action']} với {test_data}")
                r = session.post(form_info["action"], data=test_data, timeout=15)
                slug = form_info["action"].rsplit("/", 1)[-1] or "submit"
                fpath = RAW_API / f"submit_{slug}.html"
                fpath.write_text(r.text, encoding="utf-8")
                snippet = r.text[:500]
                RESULT["score_submit"].append({
                    "action": form_info["action"],
                    "data_sent": test_data,
                    "response_snippet": snippet
                })
                log.info(f"  ✅ Response ({len(r.text)} chars): {snippet[:200]}")

                # Parse response tìm điểm
                soup = BeautifulSoup(r.text, "lxml")
                scores = re.findall(r'(\d+[.,]\d*)\s*(điểm|diem|score|đ|điểm)', r.text, re.IGNORECASE)
                if scores:
                    log.info(f"    📊 Điểm tìm thấy: {scores}")
            except Exception as e:
                log.error(f"  ❌ {e}")

# ══════════════════════════════════════════════════════════
# 5. XUẤT BÁO CÁO
# ══════════════════════════════════════════════════════════
def xuat_bao_cao():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Xây dựng markdown
    lines = []
    lines.append(f"# BÁO CÁO KHÁM PHÁ HỆ THỐNG XHTDVRB")
    lines.append(f"**Thời gian crawl:** {now}")
    lines.append(f"**Base URL:** {BASE_URL}")
    lines.append(f"**Đăng nhập:** {'✅ Thành công' if RESULT['login_success'] else '❌ Thất bại'}")
    lines.append("")
    lines.append("---")
    lines.append("## 1. THỐNG KÊ TỔNG QUAN")
    lines.append(f"- Số trang đã crawl: {len(RESULT['pages_crawled'])}")
    lines.append(f"- Số form tìm được: {len(RESULT['forms'])}")
    lines.append(f"- Số select/dropdown: {len(RESULT['selects'])}")
    lines.append(f"- Số bảng dữ liệu: {len(RESULT['tables'])}")
    lines.append(f"- Số phát hiện trong JS: {len(RESULT['js_findings'])}")
    lines.append(f"- Số trọng số tìm thấy: {len(RESULT['weights_found'])}")
    lines.append("")

    lines.append("---")
    lines.append("## 2. DANH SÁCH TRANG ĐÃ CRAWL")
    for p in RESULT["pages_crawled"]:
        lines.append(f"- {p}")
    lines.append("")

    lines.append("---")
    lines.append("## 3. FORM VÀ DROPDOWN CHI TIẾT")
    for form in RESULT["forms"]:
        lines.append(f"\n### Form: `{form['action']}` [{form['method']}]")
        lines.append(f"Trang: {form['url']}")
        for f in form["fields"]:
            opts = " / ".join([f"`{o['value']}`→{o['text']}" for o in f["options"][:15]])
            lines.append(f"- `{f['name']}` ({f['type']}): {opts}")
    lines.append("")

    lines.append("---")
    lines.append("## 4. TẤT CẢ SELECT/DROPDOWN")
    for key, opts in RESULT["selects"].items():
        lines.append(f"\n### `{key}`")
        for o in opts:
            lines.append(f"- `{o['value']}` → {o['text']}")
    lines.append("")

    lines.append("---")
    lines.append("## 5. BẢNG DỮ LIỆU")
    for tbl in RESULT["tables"]:
        lines.append(f"\n### Bảng tại: {tbl['url']}")
        lines.append("| " + " | ".join(tbl["headers"]) + " |")
        lines.append("| " + " | ".join(["---"]*len(tbl["headers"])) + " |")
        for row in tbl["rows"][:30]:
            lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    lines.append("---")
    lines.append("## 6. TRỌNG SỐ TÌM THẤY")
    for key, vals in RESULT["weights_found"].items():
        lines.append(f"- **{key}**: {vals}")
    lines.append("")

    lines.append("---")
    lines.append("## 7. PHÁT HIỆN TRONG JAVASCRIPT")
    for f in RESULT["js_findings"]:
        lines.append(f"\n### File: `{Path(f['file']).name}` — dòng {f['line']}")
        lines.append(f"```javascript")
        lines.append(f"{f['content']}")
        lines.append(f"```")
    lines.append("")

    lines.append("---")
    lines.append("## 8. API ENDPOINTS")
    for url, resp in list(RESULT["api_responses"].items())[:30]:
        lines.append(f"\n### `{url}`")
        lines.append(f"```")
        lines.append(f"{resp[:200]}")
        lines.append(f"```")
    lines.append("")

    lines.append("---")
    lines.append("## 9. KẾT QUẢ SUBMIT FORM THỬ")
    for s in RESULT["score_submit"]:
        lines.append(f"\n### Action: `{s['action']}`")
        lines.append(f"Data: `{s['data_sent']}`")
        lines.append(f"```")
        lines.append(f"{s['response_snippet'][:300]}")
        lines.append(f"```")

    md = "\n".join(lines)
    (ANALYSIS / "discovery.md").write_text(md, encoding="utf-8")
    (ANALYSIS / "discovery.json").write_text(
        json.dumps(RESULT, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("\n" + "="*60)
    print("✅ CRAWL HOÀN TẤT!")
    print(f"📄 Báo cáo: {ANALYSIS / 'discovery.md'}")
    print(f"📦 JSON: {ANALYSIS / 'discovery.json'}")
    print(f"📁 HTML: {RAW_HTML}/ ({len(list(RAW_HTML.iterdir()))} files)")
    print(f"📁 JS: {RAW_JS}/ ({len(list(RAW_JS.iterdir()))} files)")
    print(f"📁 API: {RAW_API}/ ({len(list(RAW_API.iterdir()))} files)")
    print("="*60)

# ══════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("="*60)
    print("  CRAWL THỰC TẾ HỆ THỐNG XHTDVRB")
    print(f"  URL: {BASE_URL}")
    print(f"  User: {USERNAME}")
    print(f"  Time: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("="*60)

    if not USERNAME or not PASSWORD:
        print("❌ Chưa điền USERNAME/PASSWORD trong .env")
        sys.exit(1)

    if not dang_nhap():
        print("❌ Đăng nhập thất bại!")
        sys.exit(1)

    crawl_tat_ca()
    thu_submit_form()
    xuat_bao_cao()