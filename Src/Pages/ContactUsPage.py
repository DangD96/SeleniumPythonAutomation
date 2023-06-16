from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage(object):
    def __init__(self, driver):
        self.driver = driver
        if "Contact Us" not in self.driver.title:
            raise Exception(f'This is not the contact us page. Current page is {driver.title}')

    # Locators
    CONTACT_INFO = (By.CSS_SELECTOR, "div.panel-body")

    # Methods for this page
    def getContactInfo(self):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.CONTACT_INFO), message = "Element doesn't exist.")
        return self.driver.find_element(*self.CONTACT_INFO).text
