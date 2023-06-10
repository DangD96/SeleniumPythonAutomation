# Note to self, I put chromedriver here: C:\Windows

import unittest
import time
import sys
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)

# adding the grandparent directory to the sys.path.
sys.path.append(grandparent)

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.Pages.ContactUsPage import ContactUsPage

class DemoContactPage(WebDriverSetup):
    def test_contact_page(self):
        driver = self.driver
        driver.get("https://phptravels.com/contact-us/")
        time.sleep(3)
        contact = ContactUsPage(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(contact.contact_info),message = "Element doesn't exist")
        
        try:
            assert "Email" and "Skype" in contact.getContactInfo()
        except AssertionError:
            print("Assertion failed.")

if __name__ == '__main__':
    unittest.main()
