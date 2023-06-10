# Note to self, I put chromedriver here: C:\Windows

# Standard library imports
import unittest
import time
import sys
import os

# Third party imports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# Getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)

# Adding the grandparent directory to the sys.path.
sys.path.append(grandparent)

# Local app imports
from Src.Pages.HomePage import HomePage

class DemoHomePage(unittest.TestCase):
    # Setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Chrome() # Create new driver instance every time
        self.driver.maximize_window()

    def test_Home_Page(self):
        driver = self.driver
        driver.get("https://phptravels.com/demo/")
        time.sleep(3)

        # Create an instance of the class so you can make use of the methods in the class
        home = HomePage(driver)

        companyTab = home.hoverCompanyTab() # Returns CompanyTabMenu object
        contactUs = companyTab.clickContactUs() # Returns ContactUsPage object
        time.sleep(1.5)

        # If element really isn't there then an error will be thrown (NoSuchElementException)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CompanyTabSubMenu(driver).contact_us_link), message="Did not find element.")

        # Seems to need this format for arguments[0]
        #assert driver.execute_script("return arguments[0].innerText.includes('Contact Us');", CompanyTabSubMenu(driver).contact_us_link) == True

        # Click contact us
        #CompanyTabSubMenu(driver).clickContactUs()
        #time.sleep(1.5)

        # Verify the URL
        #assert driver.execute_script("return window.location.href;") == "https://phptravels.com/contact-us"
        #time.sleep(1.5)
    
    # Tear down method to run after every test case
    def tearDown(self):
        self.driver.quit()

# Runs the test case
if __name__ == '__main__':
    unittest.main()
