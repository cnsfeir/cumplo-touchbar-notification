from abc import ABC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Scraper(ABC):
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def _wait_until_all_presences_disappear(self, element: str, time: int = 10) -> None:
        """
        Waits for all elements to disappear.
        """
        WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.XPATH, element)))
