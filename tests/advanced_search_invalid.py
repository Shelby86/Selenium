
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.advance_search_elements import AdvanceSearch

from common.base import Base
from pages.advancedsearch_values import AdvancedSearchValues


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        Base.set_up(self)
        self.wait.until(self.EC.element_to_be_clickable((By.ID, "searchText")))
        select_element = self.browser.find_element_by_id("fiscalYear")
        sel = Select(select_element)
        sel.select_by_visible_text("2016")
        self.search_button = self.browser.find_element_by_id("performSearch")
        self.clear_button = self.browser.find_element_by_id("clearSearch")
        self.download_button = self.browser.find_element_by_xpath('//a[contains(text(), "Download")]')

    def test_search_project_or_abstract_invalid(self):
        self.browser.find_element_by_id("searchText").send_keys("unicorns on unicycles")
        self.search_button.click()
        time.sleep(1)
        assert not self.download_button.is_displayed()
        self.browser.quit()

    def test_invalid_title(self):
        AdvanceSearch.get_search_method_button(self).click()
        self.browser.find_element_by_xpath('//li//strong[text()="Project Title"]').click()
        self.browser.find_element_by_id("searchText").send_keys(AdvancedSearchValues.invalid_text(self))
        self.search_button.click()
        self.search_button.click()
        time.sleep(1)
        assert not self.download_button.is_displayed()
        self.browser.quit()

    def test_abstract_invalid(self):
        AdvanceSearch.get_search_method_button(self).click()
        self.browser.find_element_by_xpath('//li//strong[text()="Abstract"]').click()
        self.browser.find_element_by_id("searchText").send_keys(AdvancedSearchValues.invalid_text(self))
        self.search_button.click()
        time.sleep(1)
        assert not self.download_button.is_displayed()
        self.browser.quit()

    def test_award_number_invalid(self):
        self.browser.find_element_by_id("awardNumber").send_keys(AdvancedSearchValues.invalid_award_numer(self))
        self.search_button.click()
        time.sleep(1)
        assert not self.download_button.is_displayed()
        self.browser.quit()

    def test_invalid_principal_or_investegator(self):
        AdvanceSearch.get_principal_investigator_dircetor(self).send_keys(AdvancedSearchValues.invalid_text(self))
        self.search_button.click()
        time.sleep(1)
        assert not self.download_button.is_displayed()
        self.browser.quit()

    def test_invalid_director(self):
        AdvanceSearch.get_principal_investigator_dircetor(AdvancedSearchValues.invalid_text(self))
        self.search_button.click()
        time.sleep(1)
        assert not self.download_button.is_displayed()
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
