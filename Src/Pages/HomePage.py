from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(object):
    def __init__(self, driver):
        pass
        
    def verifyPage(self, driver):
        # Make sure we're on the right page
        return "Book Your Free Travels" in driver.title
    
    COMPANY_TAB = (By.CSS_SELECTOR, "div.nav_left li:nth-child(5)")

    # Methods for this page
    def hoverCompanyTab(self, driver):
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(*self.COMPANY_TAB)) # unpack the COMPANY_TAB tuple into find_element's two parameters
        actions.perform()
        return self
    
    def clickCompanyTab(self, driver):
        pass
