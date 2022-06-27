import os

from dotenv import load_dotenv

from libs.cumplo import CumploScraper
from libs.webdriver import DriverFactory

if __name__ == "__main__":

    load_dotenv()
    BINARY_LOCATION = os.environ.get('BINARY_LOCATION', '')

    driver_factory = DriverFactory(BINARY_LOCATION)
    with driver_factory.get_driver() as driver:
        cumplo_scraper = CumploScraper(driver)
        print(cumplo_scraper.investment_oportunities_count())
