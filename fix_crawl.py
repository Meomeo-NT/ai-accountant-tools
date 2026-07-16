with open('/root/bds-crawler/bds_crawler_final.py', 'r') as f:
    content = f.read()

old_crawl = '''def crawl_page(page):
    url = f"{BASE_URL}?p={page}"
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.find_all("div", class_="content-item")
        results = []
        for item in items:
            try:
                link_tag = item.find("a", class_="item-title")
                if not link_tag:
                    continue
                url_tin = link_tag.get("href", "")
                ma_tin = extract_ma_tin(url_tin)
                if not ma_tin:
                    continue
                title = link_tag.get_text(strip=True)
                price = item.find("div", class_="item-price")
                area = item.find("div", class_="item-area")
                addr = item.find("div", class_="item-address")
                img = item.find("img")
                results.append({
                    "ma_tin": ma_tin,
                    "title": title,
                    "price": price.get_text(strip=True) if price else "N/A",
                    "area": area.get_text(strip=True) if area else "N/A",
                    "address": addr.get_text(strip=True) if addr else "N/A",
                    "url": url_tin,
                    "image": img.get("src", "") if img else "",
                    "crawl_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            except:
                pass
        print(f"Page {page}: {len(results)} items")
        return results
    except Exception as e:
        print(f"Page {page}: {e}")
        return []'''

new_crawl = '''def crawl_page(page):
    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/trang-{page}"
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
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
                url_tin = "https://alonhadat.com.vn" + link["href"] if link else "N/A"
                ma_tin_m = extract_ma_tin(url_tin)
                if not ma_tin_m:
                    continue
                results.append({
                    "ma_tin": ma_tin_m,
                    "title": title.get_text(strip=True) if title else "N/A",
                    "price": price.get_text(strip=True).replace("Giá:", "").strip() if price else "N/A",
                    "area": area.get_text(strip=True).replace("Diện tích:", "").strip() if area else "N/A",
                    "address": addr.get_text(strip=True) if addr else "N/A",
                    "url": url_tin,
                    "image": img.get("src", "") if img else "",
                    "crawl_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            except:
                pass
        print(f"✅ Page {page}: {len(results)} items")
        return results
    except Exception as e:
        print(f"❌ Page {page}: {e}")
        return []'''

if 'content-item' in content:
    content = content.replace(old_crawl, new_crawl)
    with open('/root/bds-crawler/bds_crawler_final.py', 'w') as f:
        f.write(content)
    print('CRAWL_FIXED')
else:
    print('PATTERN_NOT_FOUND')