from selenium.webdriver.common.by import By

class CompanyTabSubMenu(object):
    def __init__(self, driver):
        self.contact_us_link = driver.find_element(By.CSS_SELECTOR, ".jfHeader-subMenuItemLink[href='https://phptravels.com/contact-us']")
    
    def clickContactUs(self):
        self.contact_us_link.click()
