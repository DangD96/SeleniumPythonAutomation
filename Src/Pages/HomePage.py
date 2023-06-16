from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        # Make sure we're on the right page first of all
        if "Book Your Free Demo Now" and "Phptravels" not in self.driver.title: 
            raise Exception(f'This is not the home page. Current page is {self.driver.title}')
        
    # Locators
    DEMO_FORM = (By.CSS_SELECTOR, "div.demo_form")
    DEMO_FORM_FIRST_NAME = (By.CSS_SELECTOR, "input[name='first_name']")
    DEMO_FORM_LAST_NAME = (By.CSS_SELECTOR, "input[name='last_name']")
    DEMO_FORM_BUSINESS_NAME = (By.CSS_SELECTOR, "input[name='business_name']")
    DEMO_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    DEMO_FORM_SUBMIT = (By.ID, "demo")
    
    # Methods/services for this page
    def demoFormInputFirstNameValid(self, firstname):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_FIRST_NAME), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_FIRST_NAME).send_keys(firstname)
        return HomePage(self.driver) # Return HomePage object since we don't move to a different "page" after this method
    
    def demoFormInputLastNameValid(self, lastname):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_LAST_NAME), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_LAST_NAME).send_keys(lastname)
        return HomePage(self.driver)
    
    def demoFormInputBusinessNameValid(self, businessname):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_BUSINESS_NAME), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_BUSINESS_NAME).send_keys(businessname)
        return HomePage(self.driver)
    
    def demoFormInputEmailValid(self, email):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_EMAIL), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_EMAIL).send_keys(email)
        return HomePage(self.driver)

    def demoFormSubmitValid(self):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_SUBMIT).click()
        return HomePage(self)
    