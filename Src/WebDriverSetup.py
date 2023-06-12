from selenium import webdriver
import unittest

class WebDriverSetup(unittest.TestCase):
    # Setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Chrome() # create new instance of webdriver
        self.driver.maximize_window()

    # Tear down method to run after every test case
    def tearDown(self):
        self.driver.quit()
