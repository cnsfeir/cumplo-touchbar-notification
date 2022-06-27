import logging
import os
from collections.abc import Iterator
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class DriverFactory:
    def __init__(self, binary_location: str) -> None:
        self.binary_location: str = binary_location
        self._silence_driver_manager()

    @contextmanager
    def get_driver(self) -> Iterator:
        options = self._get_options()
        service = self._get_service()
        try:
            driver = webdriver.Chrome(service=service, options=options)
            yield driver
        finally:
            driver.quit()

    def _get_options(self) -> ChromeOptions:
        options = ChromeOptions()
        options.add_argument('--headless')
        options.binary_location = self.binary_location
        return options

    @staticmethod
    def _get_service() -> Service:
        manager = ChromeDriverManager(chrome_type=ChromeType.BRAVE)
        return Service(manager.install())

    @staticmethod
    def _silence_driver_manager() -> None:
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        os.environ['WDM_LOG'] = "false"
