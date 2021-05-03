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

class MyTestCase(Base,unittest.TestCase):

    def setUp(self) -> None:
        Base.set_up(self)
        self.wait.until(self.EC.element_to_be_clickable((By.ID, "searchText")))
        select_element = self.browser.find_element_by_id("fiscalYear")
        sel = Select(select_element)
        sel.select_by_visible_text("2016")
        self.search_button = self.browser.find_element_by_id("performSearch")
        self.clear_button = self.browser.find_element_by_id("clearSearch")
        self.download_button = self.browser.find_element_by_xpath('//a[contains(text(), "Download")]')

    def test_search_project_title_or_abstract_valid(self):
        self.browser.find_element_by_id("searchText").send_keys(AdvancedSearchValues.valid_abstract_or_title(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_search_project_title(self):
        AdvanceSearch.get_search_method_button(self).click()
        self.browser.find_element_by_xpath('//li//strong[text()="Project Title"]').click()
        self.browser.find_element_by_id("searchText").send_keys(AdvancedSearchValues.valid_title(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_search_abstract(self):
        AdvanceSearch.get_search_method_button(self).click()
        self.browser.find_element_by_xpath('//li//strong[text()="Abstract"]').click()
        self.browser.find_element_by_id("searchText").send_keys(AdvancedSearchValues.valid_abstract(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()


    def test_award_number(self):
        self.browser.find_element_by_id("awardNumber").send_keys(AdvancedSearchValues.valid_award_number(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_recieptient_organization(self):
        self.browser.find_element_by_id("recipientOrg").send_keys(AdvancedSearchValues.valid_rec_org(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_potentional_period_of_performance_start_date(self):
        self.browser.find_element_by_id('fromDate').click()
        AdvanceSearch.select_date(self,2016,"May", 10)
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_potentional_period_of_performane_end_date(self):
        AdvanceSearch.get_date_options_button(self).click()
        self.browser.find_element_by_xpath('//*[contains(text(),"Potential Period of Performance End Date")]').click()
        self.browser.find_element_by_id('toDate').click()
        AdvanceSearch.select_date(self, 2016, "July", 15)
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_record_created_date(self):
        AdvanceSearch.get_date_options_button(self).click()
        self.browser.find_element_by_xpath('//*[contains(text(),"Record Created Date")]').click()
        self.browser.find_element_by_id('fromDate').click()
        AdvanceSearch.select_date(self, 2016, "May", 10)
        self.browser.find_element_by_id('toDate').click()
        AdvanceSearch.select_date(self, 2016, "July", 15)
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_record_modified_date(self):
        AdvanceSearch.get_date_options_button(self).click()
        self.browser.find_element_by_xpath('//*[contains(text(),"Record Modified")]').click()
        self.browser.find_element_by_id('fromDate').click()
        AdvanceSearch.select_date(self, 2016, "May", 10)
        self.browser.find_element_by_id('toDate').click()
        AdvanceSearch.select_date(self, 2016, "July", 15)
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_principal_investigator_or_project_director(self):
        AdvanceSearch.get_principal_investigator_dircetor(self).send_keys("Smith")
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_project_director(self):
        AdvanceSearch.get_principal_investigator_dircetor(self).send_keys("Bethany Smith")
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    # def test_principal_invesigator(self):
    #     pass
    #

    def test_anticipated_award_minimun(self):
        self.browser.find_element_by_id("awardAmountFrom").send_keys(AdvancedSearchValues.maximum(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_anticipated_award_maximum(self):
        AdvanceSearch.get_award_maximum(self).send_keys(AdvancedSearchValues.maximum(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    def test_anticipated_award_min_and_max(self):
        AdvanceSearch.get_award_minmim(self).send_keys(AdvancedSearchValues.minimun(self))
        AdvanceSearch.get_award_maximum(self).send_keys(AdvancedSearchValues.maximum(self))
        self.search_button.click()
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        results = AdvanceSearch.get_results(self)
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()


    # def test_dod_awarding_offices(self):
        select_element = self.browser.find_element_by_xpath("//select[@id='dodAwardingOffice']")
        # This is an example of how to iterate through every item in a drop down
        # This will verify the UI works but will not do any data validation
        options_list = self.browser.find_elements_by_xpath("//select[@id='dodAwardingOffice']//option")
        for option in options_list:
            option.click()
        # For Data validation selecting one value at a time and asserting it is a better approach
        # In the interest of time only one item is shown
        # An argument can be made that one test per item in the dropdown would be best for data validation
        select_element = self.browser.find_element_by_xpath("//select[@id='dodAwardingOffice']")
        sel = Select(select_element)
        sel.select_by_visible_text("ACC - Warren")
        self.search_button.click()
        results = AdvanceSearch.get_results(self)
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
        assert len(results) > 0
        assert self.download_button.is_displayed()
        self.browser.quit()

    # This test would be approached in a similar fashion to the one above
    # Since all but one option returned search results, a more general approach was made
    def test_dod_funding_agencies(self):
        options_list = self.browser.find_elements_by_xpath("//select[@id='fundingAgency']//option")
        for option in options_list:
            if option != self.browser.find_element_by_xpath("//select[@id='fundingAgency']//option[@label='DA-OCOE - Office of the Chief of Engineers']"):
                option.click()
                self.search_button.click()
                self.wait.until(self.EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download")]')))
                time.sleep(1)
                results = AdvanceSearch.get_results(self)
                assert len(results) > 0
                assert self.download_button.is_displayed()

if __name__ == '__main__':
    unittest.main()


