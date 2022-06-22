from libs.cumplo import CumploScraper
from libs.webdriver import DriverFactory

if __name__ == "__main__":
    with DriverFactory.get_driver() as driver:
        cumplo_scraper = CumploScraper(driver)
        print(cumplo_scraper.investment_oportunities_count())
