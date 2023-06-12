# Note to self, I put chromedriver here: C:\Windows

# Standard library imports
import unittest
import time
import sys
import os

# Third party imports here
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)

# Adding the grandparent directory to the sys.path.
sys.path.append(grandparent)

# Local app imports
from Src.Pages.HomePage import HomePage
from Src.Pages.NavigationToolbar import NavigationToolbar
from Src.WebDriverSetup import WebDriverSetup

class DemoHomePage(WebDriverSetup):
    def test_Home_Page(self):
        driver = self.driver
        driver.get("https://phptravels.com/demo/")
        time.sleep(3)

        home = HomePage(driver)
        navBar = NavigationToolbar(driver)
        navBar.hoverCompanyTab()
        contactUs = navBar.clickContactUs() # Returns ContactUsPage object
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

# Runs the test case
if __name__ == '__main__':
    unittest.main()
