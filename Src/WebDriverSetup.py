from selenium import webdriver
import unittest

class WebDriverSetup(unittest.TestCase):
    driver = webdriver.Edge() # arbitrary browser driver
    
    # Tear down method to run after every test case
    def tearDown(self):
        self.driver.quit()

class WebDriverSetupChrome(WebDriverSetup):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

class WebDriverSetupFirefox(WebDriverSetup):
    # Setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

class WebDriverSetupEdge(WebDriverSetup):
    # Setup method that runs before every test case
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
