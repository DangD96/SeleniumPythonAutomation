from selenium.webdriver.common.by import By
from .ContactUsPage import ContactUsPage
from selenium.webdriver.common.action_chains import ActionChains

class NavigationToolbar(object):
    def __init__(self, driver):
        self.driver = driver

    # Locators
    COMPANY_TAB = (By.CSS_SELECTOR, "div.nav_left li:nth-child(5)")
    COMPANY_TAB_CONTACT_US = (By.CSS_SELECTOR, "[href='https://phptravels.com/contact-us']")

    # Page methods/services
    def hoverCompanyTab(self):
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element(*self.COMPANY_TAB)) # unpack the COMPANY_TAB tuple into find_element's two parameters
            actions.perform()
            return NavigationToolbar(self.driver)

    def clickContactUs(self):
        self.driver.find_element(*self.COMPANY_TAB_CONTACT_US).click()
        return ContactUsPage(self.driver) # Return ContactUsPage object because this action takes us to that "page" now
    
    
        