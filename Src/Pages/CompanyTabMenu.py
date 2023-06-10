from selenium.webdriver.common.by import By
from .ContactUsPage import ContactUsPage

class CompanyTabMenu(object):
    def __init__(self, driver):
        self.driver = driver

    # Locators
    CONTACT_US_LINK = (By.CSS_SELECTOR, "[href='https://phptravels.com/contact-us']")
    
    # Page methods/services
    def clickContactUs(self):
        self.driver.find_element(*self.CONTACT_US_LINK).click()
        return ContactUsPage(self.driver)
