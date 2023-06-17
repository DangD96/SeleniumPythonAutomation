from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage

class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        if "Contact Us" not in self.driver.title:
            raise Exception(f'This is not the contact us page. Current page is {self.driver.title}')

    # Locators
    CONTACT_INFO = (By.CSS_SELECTOR, "div.panel-body")

    # Methods for this page
    def getContactInfo(self):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.CONTACT_INFO), message = "Element doesn't exist.")
        return self.driver.find_element(*self.CONTACT_INFO).text
