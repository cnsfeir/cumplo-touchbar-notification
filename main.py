from libs.cumplo import CumploScraper

if __name__ == "__main__":
    cumplo_scraper = CumploScraper()
    try:
        print(cumplo_scraper.investment_oportunities_count())
    except Exception:
        cumplo_scraper.free_driver()
    else:
        cumplo_scraper.free_driver()
