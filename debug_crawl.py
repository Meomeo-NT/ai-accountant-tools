import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://alonhadat.com.vn/can-ban-nha-dat/khanh-hoa"
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)"

for page in [1, 2]:
    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/trang-{page}"
    
    print(f"\n=== Page {page}: {url} ===")
    resp = requests.get(url, headers={"User-Agent": UA}, timeout=10)
    print(f"Status: {resp.status_code}, Length: {len(resp.text)}")
    resp.encoding = "utf-8"
    
    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.find_all("article", class_="property-item")
    print(f"article.property-item: {len(items)}")
    
    # Check if property-title exists
    titles = soup.find_all("h3", class_="property-title")
    print(f"h3.property-title: {len(titles)}")
    
    # Check link tags
    links = soup.find_all("a", class_="link")
    print(f"a.link: {len(links)}")
    
    # Show first item
    if items:
        item = items[0]
        print(f"\nFirst item:")
        print(f"  title: {item.find('h3', class_='property-title')}")
        print(f"  link: {item.find('a', class_='link')}")
        print(f"  price: {item.find('span', class_='price')}")