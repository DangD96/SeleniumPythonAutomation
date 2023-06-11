from selenium import webdriver
import unittest

class WebDriverSetupChome(unittest.TestCase):
    # Setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Tear down method to run after every test case
    def tearDown(self):
        self.driver.quit()
