from selenium.webdriver.common.by import By

class ContactUsPage(object):
    def __init__(self, driver):
        self.driver = driver

    # Locators
    CONTACT_INFO = (By.CSS_SELECTOR, "div.panel-body")

    # Methods for this page
    def verifyPage(self):
        return "Contact Us" in self.driver.title
    
    def getContactInfo(self):
        return self.driver.find_element(*self.CONTACT_INFO).text
