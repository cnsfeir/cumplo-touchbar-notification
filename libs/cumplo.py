from collections.abc import Iterator

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

Oportunity = tuple[WebElement, WebElement, WebElement]


class CumploScraper(Scraper):
    def _wait_loading_animation(self) -> bool:
        try:
            self._wait_until_all_presences_disappear(CUMPLO_LOADING_SELECTOR)
        except TimeoutException:
            return False
        else:
            return True

    def _get_oportunities(self) -> Iterator[Oportunity]:
        tirs = self.driver.find_elements(By.XPATH, TIR_XPATH)
        grades = self.driver.find_elements(By.XPATH, GRADES_XPATH)
        progress = self.driver.find_elements(By.XPATH, PROGRESS_XPATH)
        return zip(tirs, grades, progress)

    @staticmethod
    def _is_complete(progress: WebElement) -> bool:
        return get_percentage(progress) >= 100

    @staticmethod
    def _is_promising(tir: WebElement, grade: WebElement) -> bool:
        promising_tir: bool = get_percentage(tir) >= TIR_THRESHOLD
        promising_grade: bool = get_percentage(grade) >= GRADE_THRESHOLD
        return promising_tir and promising_grade

    def investment_oportunities_count(self) -> int:
        self.driver.get(INVESTMENT_OPORTUNITIES_URL)
        oportunities_count = 0
        if self._wait_loading_animation():
            for tir, grade, progress in self._get_oportunities():
                if self._is_complete(progress):
                    continue
                if self._is_promising(tir, grade):
                    oportunities_count += 1
        return oportunities_count
