import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import os




class Base(unittest.TestCase):

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def set_up(self):
        TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        PROJ_DIR = os.path.dirname(TEST_DIR)
        CHROME_DRIVER = PROJ_DIR + '/browsers/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        self.browser = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER)
        self.base_url = ('https://dodgrantawards.dtic.mil/grants/index.html#/advancedSearch')
        self.wait = WebDriverWait(self.browser, 30)
        self.EC = expected_conditions
        self.browser.get(self.base_url)






