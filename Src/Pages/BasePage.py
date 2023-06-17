class BasePage(object):
    def __init__(self, driver):
        self.driver = driver # Put in Base class so don't have to type out every time
