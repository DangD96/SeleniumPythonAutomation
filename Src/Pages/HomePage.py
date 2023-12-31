import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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
        first_name_field = self.driver.find_element(*self.DEMO_FORM_FIRST_NAME)
        first_name_field.send_keys(firstname)
        time.sleep(3)
    
    def demoFormInputLastNameValid(self, lastname):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_LAST_NAME), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_LAST_NAME).send_keys(lastname)
        time.sleep(3)
    
    def demoFormInputBusinessNameValid(self, businessname):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_BUSINESS_NAME), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_BUSINESS_NAME).send_keys(businessname)
        time.sleep(3)
    
    def demoFormInputEmailValid(self, email):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM_EMAIL), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_EMAIL).send_keys(email)
        time.sleep(3)

    def demoFormSubmitValid(self):
        WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*self.DEMO_FORM), message = "Element doesn't exist.")
        self.driver.find_element(*self.DEMO_FORM_SUBMIT).click()
    