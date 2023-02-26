from selenium.webdriver.remote.webelement import WebElement


def get_percentage(element: WebElement) -> float:
    """
    Returns the percentage of a given element.
    """
    return float(element.get_attribute("innerText").replace("%", ""))
