from selenium.webdriver.remote.webelement import WebElement


def get_percentage(element: WebElement) -> float:
    return float(element.get_attribute('innerText').replace('%', ''))
