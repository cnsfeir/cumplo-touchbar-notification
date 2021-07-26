from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class CumploScraper():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        self.driver = webdriver.Chrome(executable_path='/opt/drivers/chromedriver', options=options)

    def free_driver(self):
        self.driver.quit() if self.driver else None

    def wait_untilall_presences_disappears(self, element: str, element_type: str, time: int=10):
        if element_type == "ID":
            return WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.ID, element)))
        elif element_type == "CSS_SELECTOR":
            return WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.CSS_SELECTOR, element)))
        elif element_type == "CLASS_NAME":
            return WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.CLASS_NAME, element)))
        elif element_type == "NAME":
            return WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.NAME, element)))
        elif element_type == "XPATH":
            return WebDriverWait(self.driver, time).until_not(ec.presence_of_all_elements_located((By.XPATH, element)))
    
    def wait_loading_animation(self):
        try:
            # print('WAITING FOR ANIMATION TO DISAPPEAR...')
            self.wait_untilall_presences_disappears("//*[contains(@class, 'MuiCircularProgress')]", 'XPATH')
        except TimeoutException:
            return False
        else:
            #print('DONE! CONTINUING...')
            return True

    def investment_oportunities_count(self) -> int:
        oportunities_count = 0
        # print('\n')
        # print('GOING TO URL...')
        self.driver.get('https://cumplo.cl/oportunidades-de-inversion/')
        if self.wait_loading_animation():
            oportunities = self.driver.find_elements_by_xpath("//span[text()='Financiado']/preceding-sibling::span")
            get_percentage = lambda x: int(x.get_attribute('innerText').replace('%', ''))
            # print('GETTING PERCENTAGES:')
            for percentage in map(get_percentage, oportunities):
                #print(percentage)
                if percentage < 100:
                    oportunities_count += 1
        return oportunities_count
