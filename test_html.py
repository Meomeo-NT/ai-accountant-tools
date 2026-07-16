import requests
from bs4 import BeautifulSoup

r = requests.get('https://alonhadat.com.vn/can-ban-nha-dat/khanh-hoa', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')

# Test selectors
for tag_name, cls in [('article', 'property-item'), ('div', 'content-item'), ('div', 're__card-info'), ('a', 're__card-title'), ('div', 're__card-config'), ('div', 'js__card-body')]:
    items = soup.find_all(tag_name, class_=cls)
    print(f'{tag_name}.{cls}: {len(items)}')

# Find any tag with "item" in class
for tag in soup.find_all(True)[:500]:
    c = tag.get('class')
    if c and any('item' in x.lower() or 'card' in x.lower() for x in c):
        print(f'\nSample: {tag.name}.{" ".join(c)}')
        print(tag.get_text()[:100])
        break