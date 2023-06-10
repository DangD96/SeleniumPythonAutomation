from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .CompanyTabMenu import CompanyTabMenu

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        # Make sure we're on the right page first of all
        if "Book Your Free Demoss Now" not in driver.title: 
            raise Exception(f'This is not the home page. Current page is {driver.title}')
        
    # Locators
    COMPANY_TAB = (By.CSS_SELECTOR, "div.nav_left li:nth-child(5)")
    
    # Methods/services for this page
    def hoverCompanyTab(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.COMPANY_TAB)) # unpack the COMPANY_TAB tuple into find_element's two parameters
        actions.perform()
        return CompanyTabMenu(self.driver) # Return CompanyTabMenu object since we're at that "page" now
    
