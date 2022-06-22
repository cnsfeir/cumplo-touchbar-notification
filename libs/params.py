# THRESHOLDS
TIR_THRESHOLD: float = 7.5
GRADE_THRESHOLD: float = 0.4

# ELEMENTS
TIR_XPATH: str = "//p[text()='TIR']/preceding-sibling::p"
GRADES_XPATH: str = "//p[text()='Calificación']/preceding-sibling::p"
PROGRESS_XPATH: str = "//span[text()='Financiado']/preceding-sibling::span"
CUMPLO_LOADING_SELECTOR: str = "//*[contains(@class, 'MuiCircularProgress')]"

# URL
INVESTMENT_OPORTUNITIES_URL: str = 'https://cumplo.cl/oportunidades-de-inversion/'
