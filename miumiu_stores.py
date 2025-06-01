import requests
from bs4 import BeautifulSoup

def scrape_miumiu_stores():
    url = "https://www.miumiu.com/us/en/store-locator/united-states.html"
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, "html.parser")
    stores = []
    h2s = soup.find_all("h2")
    print(f"[MiuMiu] 抓到 h2 数量: {len(h2s)}")
    for h2 in h2s:
        name = h2.get_text(strip=True)
        address = ""
        phone = ""
        # MiuMiu 结构可能不同，尝试多种方式
        p = h2.find_next_sibling("p")
        if p:
            address = p.get_text(strip=True)
            next_tag = p.find_next_sibling()
            while next_tag and next_tag.name != "p":
                if next_tag.name == "span":
                    phone = next_tag.get_text(strip=True)
                    break
                next_tag = next_tag.find_next_sibling()
        if name and address:
            stores.append(f"{name}\n{address}\n{phone}")
    with open("miumiu_stores.txt", "w", encoding="utf-8") as f:
        for store in stores:
            f.write(store + "\n\n")
    print(f"[MiuMiu] 成功抓取门店数量: {len(stores)}")
    if len(stores) == 0:
        print("[MiuMiu] 没有抓到门店数据，可能页面结构已变或为JS渲染。建议手动检查页面源码。")

if __name__ == "__main__":
    scrape_miumiu_stores()