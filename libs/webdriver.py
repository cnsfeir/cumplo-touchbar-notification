import os
from contextlib import contextmanager
from collections.abc import Iterator

from dotenv import load_dotenv
from selenium.webdriver import Chrome, ChromeOptions

load_dotenv()
DRIVER_LOCATION = os.environ.get('DRIVER_LOCATION', '')
BINARY_LOCATION = os.environ.get('BINARY_LOCATION', '')


class DriverFactory:
    @classmethod
    @contextmanager
    def get_driver(cls) -> Iterator:
        options = cls._get_options()
        try:
            driver = Chrome(executable_path=DRIVER_LOCATION, options=options)
            yield driver
        finally:
            driver.quit()

    @staticmethod
    def _get_options() -> ChromeOptions:
        options = ChromeOptions()
        options.add_argument('--headless')
        options.binary_location = BINARY_LOCATION
        return options
