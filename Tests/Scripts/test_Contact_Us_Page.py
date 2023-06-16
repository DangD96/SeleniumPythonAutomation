# Note to self, I put chromedriver here: C:\Windows

import unittest
import time
import sys
import os

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)

# adding the grandparent directory to the sys.path.
sys.path.append(grandparent)

from Src.Pages.ContactUsPage import ContactUsPage
from Src.WebDriverSetup import WebDriverSetup

class DemoContactPage(WebDriverSetup):
    def test_contact_page(self):
        driver = self.driver
        driver.get("https://phptravels.com/contact-us/")
        time.sleep(3)
        contact = ContactUsPage(driver)
        assert "Email" and "Phone" in contact.getContactInfo()


if __name__ == '__main__':
    unittest.main()
