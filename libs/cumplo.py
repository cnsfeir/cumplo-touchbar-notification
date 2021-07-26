import os
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class CumploScraper():
    def __init__(self):
        load_dotenv(find_dotenv())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.binary_location = os.environ.get('BINARY_LOCATION')
        self.driver = webdriver.Chrome(executable_path=os.environ.get('DRIVER_LOCATION'), options=options)

    def free_driver(self):
        self.driver.quit() if self.driver else None

    def wait_until_all_presences_disappears(self, element: str, time: int=10):
        WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.XPATH, element)))
    
    def wait_loading_animation(self):
        try:
            self.wait_until_all_presences_disappears("//*[contains(@class, 'MuiCircularProgress')]")
        except TimeoutException:
            return False
        else:
            return True

    def investment_oportunities_count(self) -> int:
        oportunities_count = 0
        self.driver.get('https://cumplo.cl/oportunidades-de-inversion/')
        if self.wait_loading_animation():
            oportunities = self.driver.find_elements_by_xpath("//span[text()='Financiado']/preceding-sibling::span")
            get_percentage = lambda x: int(x.get_attribute('innerText').replace('%', ''))
            for percentage in map(get_percentage, oportunities):
                if percentage < 100:
                    oportunities_count += 1
        return oportunities_count
