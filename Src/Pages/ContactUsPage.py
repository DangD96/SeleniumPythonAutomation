from selenium.webdriver.common.by import By

class ContactUsPage(object):
    def __init__(self, driver):
        self.contact_info = driver.find_element(By.CSS_SELECTOR, "div.panel-body") 

    # Methods for this page
    def getContactInfo(self):
        return self.contact_info.text
