from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class AdvanceSearch():

    def get_search_button(self):
        search_button = self.browser.find_elements_by_id("performSearch")
        return(search_button)

    def get_clear_button(self):
        clear_button = self.browser.find_element_by_id("clearSearch")
        return clear_button

    def get_download_button(self):
        download_button = self.browser.find_element_by_xpath('//a[contains(text(), "Download")]')
        return download_button

    def get_search_method_button(self):
        button = self.browser.find_element_by_xpath('//*[contains(text(),"Search Method")]')
        return button

    def get_results(self):
        results = self.browser.find_elements_by_xpath('//div[@class="panel search-result ng-scope"]')
        return(results)

    def get_date_options_button(self):
        date_options_button = self.browser.find_element_by_xpath('//*[contains(@title, "Select which date")]')
        return date_options_button

    def select_date(self, year, month, date):
        self.browser.find_element_by_xpath("//button[contains(@id, 'datepicker')]").click()
        self.browser.find_element_by_xpath('//button[contains(@id, "datepicker")]').click()
        self.browser.find_element_by_xpath('//button[@class="btn btn-default btn-sm pull-left"]').click()
        self.browser.find_element_by_xpath(f"//span[text()='{year}']").click()
        time.sleep(2)
        self.browser.find_element_by_xpath(f"//span[text()='{month}']").click()
        self.browser.find_element_by_xpath(f'//span[text()="{date}"]').click()

    def get_principal_investigator_dircetor(self):
        name = self.browser.find_element_by_id('poc')
        return name

    def get_award_minmim(self):
        name = self.browser.find_element_by_id("awardAmountFrom")
        return name

    def get_award_maximum(self):
        name = self.browser.find_element_by_id("awardAmountTo")
        return name


