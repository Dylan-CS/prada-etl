from prada_stores import scrape_all_prada_stores
from miumiu_stores import scrape_miumiu_stores
from versace_stores import scrape_versace_stores

if __name__ == "__main__":
    print("Start scraping Prada stores...")
    scrape_all_prada_stores()
    print("Prada done. Start scraping Miumiu stores...")
    scrape_miumiu_stores()
    print("Miumiu done. Start scraping Versace stores...")
    # scrape_versace_stores()
    print("All done.") 