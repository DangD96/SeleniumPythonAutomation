from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage

class NavigationToolbar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    COMPANY_TAB = (By.CSS_SELECTOR, "div.nav_left li:nth-child(5)")
    COMPANY_TAB_CONTACT_US = (By.CSS_SELECTOR, "[href='https://phptravels.com/contact-us']")

    # Page methods/services
    def hoverCompanyTab(self):
        # Wait until the callable function returns something that evals to True
        # Use * to unpack the COMPANY_TAB tuple into find_element's two parameters
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*self.COMPANY_TAB), message="Could not find element.") 
        companyTab = self.driver.find_element(*self.COMPANY_TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(companyTab) 
        actions.perform()

    def clickContactUs(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*self.COMPANY_TAB_CONTACT_US), message="Could not find element.")
        contactUsLink = self.driver.find_element(*self.COMPANY_TAB_CONTACT_US)
        contactUsLink.click()
        