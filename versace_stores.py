# Updated Versace scraping function in scraper.py
import requests

def scrape_versace_stores():
    print("[DEBUG] Versace 爬虫开始")
    url = "https://www.versace.com/ww/en/store-locator/_jcr_content/stores.stores.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers)
        print(f"[DEBUG] Status code: {resp.status_code}")
        print(f"[DEBUG] Response length: {len(resp.text)}")
        try:
            data = resp.json()
        except Exception as e:
            print("[DEBUG] JSON decode error:", e)
            print("[DEBUG] Status code:", resp.status_code)
            print("[DEBUG] Response text:", resp.text[:1000])
            return
        stores = []
        country_counts = {}
        for store in data.get("stores", []):
            name = store.get("name", "")
            address = store.get("address", "")
            city = store.get("city", "")
            country = store.get("country", "")
            phone = store.get("phone", "")
            stores.append(f"{name}\n{address}, {city}, {country}\n{phone}")
            country_counts[country] = country_counts.get(country, 0) + 1
        with open("versace_stores.txt", "w", encoding="utf-8") as f:
            for store in stores:
                f.write(store + "\n\n")
        print(f"[Versace] 全球门店数量: {len(stores)}")
        for c, n in country_counts.items():
            print(f"  {c}: {n}")
        if len(stores) == 0:
            print("[Versace] 没有抓到门店数据，API 可能已变。请手动检查接口。")
    except Exception as e:
        print(f"[DEBUG] requests 异常: {e}")
    print("[DEBUG] Versace 爬虫结束")
    return

if __name__ == "__main__":
    scrape_versace_stores()
