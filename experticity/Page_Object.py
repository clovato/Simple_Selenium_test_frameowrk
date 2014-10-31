import test
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils import Utilities
from testtools import matchers
from selenium.webdriver.common.keys import Keys
_rgf = Utilities.reg_finder
_src = test.TestCase.get_page_src

class Experticity(test.TestCase, object):

    def homepage(self, url):
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()

    def email(self, value):
        element = self.driver.find_element(By.ID, "email")
        element.clear()
        element.send_keys(value)
        self.email = value


    def first_name(self, value):
        element = self.driver.find_element(By.ID, "firstName")
        element.clear()
        element.send_keys(value)
        self._first_name = value

    def last_name(self, value):
        element = self.driver.find_element(By.ID, "lastName")
        element.clear()
        element.send_keys(value)
        self._last_name = value

    def user_name(self, value):
        element = self.driver.find_element(By.ID, "userName")
        element.clear()
        element.send_keys(value)
        self._user_name = value

    def password(self, value):
        element = self.driver.find_element(By.ID, "password")
        element.clear()
        element.send_keys(value)
        self._password = value

    def confirm(self, value):
        element = self.driver.find_element(By.ID, "passwordConfirmation")
        element.clear()
        element.send_keys(value)
        self._confirm = value

    def position(self, value):
        select = Select(self.driver.find_element(By.ID, "jobFunctionId"))
        select.select_by_visible_text(value)
        self._position = value

    def status(self, value):
        select = Select(self.driver.find_element(By.ID, "employmentStatus"))
        select.select_by_visible_text(value)
        self._status = value

    def hire_date(self, value):
        element = self.driver.find_element(By.ID, "hireDate")
        element.clear()
        element.send_keys(value)
        self._hire_date = value

    def referral(self, value):
        select = Select(self.driver.find_element(By.ID, "referringAgentId"))
        select.select_by_visible_text(value)
        self._status = value

    def referral_code(self, value):
        element = self.driver.find_element(By.ID, "referralCode")
        element.clear()
        element.send_keys(value)
        self._referral_code = value

    def referral_code_click(self):
        self.driver.find_element(By.ID, "referralCode").click()

    def click_next(self):
        self.driver.find_element(By.ID, "next-btn").click()

    def search_store(self, store):
        element = self.driver.find_element(By.ID, 'searchInput')
        element.send_keys(store)
        element.send_keys(Keys.RETURN)

    def select_store(self, store):
        element = self.driver.find_element(By.CSS_SELECTOR, "#select_location")
        element.click()

    def submit_form(self):
        element = self.driver.find_element(By.XPATH, "//input[@value='Confirm']")
        element.click()

    def final_submit(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
        element.click()

    def assert_expertise(self):
        expected_value = "Build Your Expertise"
        actual_value = self.driver.find_element(By.CSS_SELECTOR, "h1.taxonomyPickerName").text
        self.expectThat(actual_value, matchers.Equals(expected_value))
        print("sign up test passed!!!!!")