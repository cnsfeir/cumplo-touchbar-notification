# THRESHOLDS
TIR_THRESHOLD: float = 22.0
GRADE_THRESHOLD: float = 0.4

# ELEMENTS
TIR_XPATH: str = "//span[text()[contains(.,'TIR')]]/preceding-sibling::p"
GRADES_XPATH: str = "//span[text()[contains(.,'Calificación')]]/preceding-sibling::p"
PROGRESS_XPATH: str = "//span[text()[contains(.,'Financiado')]]/preceding-sibling::span"
CUMPLO_LOADING_SELECTOR: str = "//*[contains(@class, 'MuiCircularProgress')]"

# URL
INVESTMENT_OPORTUNITIES_URL: str = "https://cumplo.cl/oportunidades-de-inversion/"
