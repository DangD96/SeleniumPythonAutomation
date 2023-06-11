from selenium.webdriver.common.by import By

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        # Make sure we're on the right page first of all
        if "Book Your Free Demo Now" and "Phptravels" not in driver.title: 
            raise Exception(f'This is not the home page. Current page is {driver.title}')
        
    # Locators
    DEMO_FORM = (By.CSS_SELECTOR, "div.demo_form")
    DEMO_FORM_FIRST_NAME = (By.CSS_SELECTOR, "input[name='first_name']")
    DEMO_FORM_LAST_NAME = (By.CSS_SELECTOR, "input[name='last_name']")
    DEMO_FORM_BUSINESS_NAME = (By.CSS_SELECTOR, "input[name='business_name']")
    DEMO_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    
    # Methods/services for this page
    def demoFormInputFirstNameValid(self):
        return HomePage(self.driver) # Return HomePage object since we don't move to a different "page" after this method
    
    def demoFormInputLastNameValid(self):
        return HomePage(self.driver)
    
    def demoFormInputBusinessNameValid(self):
        return HomePage(self.driver)
    
    def demoFormInputEmailValid(self):
        return HomePage(self.driver)

    def demoFormSubmitValid(self):
        return HomePage(self)