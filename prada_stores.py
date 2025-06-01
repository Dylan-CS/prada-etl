import requests
from bs4 import BeautifulSoup

def scrape_prada_stores():
    url = "https://www.prada.com/us/en/store-locator/united-states.html"
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, "html.parser")
    stores = []
    # Prada 美国区页面结构：每个门店以 h2（门店名）+ 地址+电话+"See details"分组
    for h2 in soup.find_all("h2"):
        name = h2.get_text(strip=True)
        # 地址和电话在下方的 p、span、text 节点
        address = ""
        phone = ""
        p = h2.find_next_sibling("p")
        if p:
            address = p.get_text(strip=True)
            # 电话通常在下一个 sibling
            next_tag = p.find_next_sibling()
            while next_tag and next_tag.name != "p":
                if next_tag.name == "span":
                    phone = next_tag.get_text(strip=True)
                    break
                next_tag = next_tag.find_next_sibling()
        if name and address:
            stores.append(f"{name}\n{address}\n{phone}")
    with open("prada_stores.txt", "w", encoding="utf-8") as f:
        for store in stores:
            f.write(store + "\n\n")

if __name__ == "__main__":
    scrape_prada_stores()
