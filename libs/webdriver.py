import os
from collections.abc import Iterator
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class DriverFactory:
    def __post_init__(self) -> None:
        os.environ["WDM_LOG"] = "false"

    @contextmanager
    def get_driver(self) -> Iterator:
        """
        Returns a context manager that yields a Chrome driver.
        """
        options = self._get_options()
        service = self._get_service()
        try:
            driver = webdriver.Chrome(service=service, options=options)
            yield driver
        finally:
            driver.quit()

    def _get_options(self) -> ChromeOptions:
        options = ChromeOptions()
        options.add_argument("--headless")
        return options

    @staticmethod
    def _get_service() -> Service:
        manager = ChromeDriverManager(chrome_type=ChromeType.BRAVE)
        return Service(manager.install())
