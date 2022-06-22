from collections.abc import Iterator

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from libs.utils import get_percentage
from libs.params import (
    TIR_XPATH,
    GRADES_XPATH,
    TIR_THRESHOLD,
    PROGRESS_XPATH,
    GRADE_THRESHOLD,
    CUMPLO_LOADING_SELECTOR,
    INVESTMENT_OPORTUNITIES_URL,
)
from libs.scraper import Scraper

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
        tirs = self.driver.find_elements_by_xpath(TIR_XPATH)
        grades = self.driver.find_elements_by_xpath(GRADES_XPATH)
        progress = self.driver.find_elements_by_xpath(PROGRESS_XPATH)
        return zip(tirs, grades, progress)

    @staticmethod
    def _is_complete(progress: WebElement) -> bool:
        return get_percentage(progress) >= 100

    @staticmethod
    def _is_interesting(tir: WebElement, grade: WebElement) -> bool:
        interesting_tir: bool = get_percentage(tir) >= TIR_THRESHOLD
        interesting_grade: bool = get_percentage(grade) >= GRADE_THRESHOLD
        return interesting_tir and interesting_grade

    def investment_oportunities_count(self) -> int:
        self.driver.get(INVESTMENT_OPORTUNITIES_URL)
        oportunities_count = 0
        if self._wait_loading_animation():
            for tir, grade, progress in self._get_oportunities():
                if self._is_complete(progress):
                    continue
                if self._is_interesting(tir, grade):
                    oportunities_count += 1
        return oportunities_count
