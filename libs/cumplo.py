from collections.abc import Iterator
from logging import getLogger

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from libs.params import (
    CUMPLO_LOADING_SELECTOR,
    GRADE_THRESHOLD,
    GRADES_XPATH,
    INVESTMENT_OPORTUNITIES_URL,
    PROGRESS_XPATH,
    TIR_THRESHOLD,
    TIR_XPATH,
)
from libs.scraper import Scraper
from libs.utils import get_percentage

logger = getLogger(__name__)

Oportunity = tuple[WebElement, WebElement, WebElement]


class CumploScraper(Scraper):
    def _wait_loading_animation(self) -> bool:
        """
        Waits for the loading animation to disappear.
        """
        try:
            logger.info("Waiting for loading animation to disappear...")
            self._wait_until_all_presences_disappear(CUMPLO_LOADING_SELECTOR)
            logger.info("Loading animation disappeared!")
            return True
        except TimeoutException:
            logger.error("Loading animation did not disappear.")
            return False

    def _get_oportunities(self) -> Iterator[Oportunity]:
        """
        Gets the information of each investment opportunity.
        """
        tirs = self.driver.find_elements(By.XPATH, TIR_XPATH)
        grades = self.driver.find_elements(By.XPATH, GRADES_XPATH)
        progress = self.driver.find_elements(By.XPATH, PROGRESS_XPATH)

        logger.info(f"Found {len(tirs)} investment opportunities.")
        return zip(tirs, grades, progress)

    @staticmethod
    def _is_complete(progress: WebElement) -> bool:
        """
        Checks if the investment opportunity is complete.
        """
        return get_percentage(progress) >= 100

    @staticmethod
    def _is_promising(tir: WebElement, grade: WebElement) -> bool:
        """
        Checks if the investment opportunity is promising.
        """
        promising_tir: bool = get_percentage(tir) >= TIR_THRESHOLD
        promising_grade: bool = get_percentage(grade) >= GRADE_THRESHOLD
        return promising_tir and promising_grade

    def investment_oportunities_count(self) -> int:
        """
        Returns the number of investment opportunities that are promising.
        """
        self.driver.get(INVESTMENT_OPORTUNITIES_URL)
        oportunities_count = 0
        if self._wait_loading_animation():
            for tir, grade, progress in self._get_oportunities():

                if self._is_complete(progress):
                    logger.info("Investment opportunity is complete.")
                    continue

                if self._is_promising(tir, grade):
                    logger.info("Investment opportunity is promising!")
                    oportunities_count += 1

        logger.info(f"Found {oportunities_count} promising investment opportunities.")
        return oportunities_count
