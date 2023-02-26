from logging import CRITICAL, DEBUG, basicConfig, getLogger

from libs.cumplo import CumploScraper
from libs.webdriver import DriverFactory

FORMAT = "\n [%(levelname)s] (%(name)s:%(lineno)d) \n %(message)s"
basicConfig(level=DEBUG, format=FORMAT)
logger = getLogger(__name__)

getLogger("WDM").setLevel(CRITICAL)
getLogger("urllib3").setLevel(CRITICAL)
getLogger("selenium").setLevel(CRITICAL)


if __name__ == "__main__":

    driver_factory = DriverFactory()
    with driver_factory.get_driver() as driver:
        cumplo_scraper = CumploScraper(driver)
        print(cumplo_scraper.investment_oportunities_count())
