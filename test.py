import os
import testtools
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import utils

FILE_PATH = os.path.abspath(os.path.dirname(__file__))
CFG =utils.parse_config(FILE_PATH + "/sys_config.ini")


class TestCase(testtools.TestCase):
    """Test case base class for all tests"""

    def setUp(self):
        """Run before each test method to initialize test env"""
        super(TestCase, self).setUp()
        browser = CFG.get("env", "browser")

        if browser == 'chrome':
            self.driver = wd.Chrome()
        elif browser == 'ie':
            self.driver = wd.Ie()
        elif browser == 'firefox':
            self.driver = wd.Firefox()

        self.driver.implicitly_wait(45)
        self.verificationErrors = []



    def waitID(self, time, element):

        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, element))
            )
        finally:
            self.driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        super(TestCase, self).tearDown()
        #self.assertEqual([], self.verificationErrors)
        #print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        #try:
            #if sys.exc_info() == (None, None, None):
                #sauce.jobs.update_job(self.driver.session_id, passed=True)
            #else:
                #sauce.jobs.update_job(self.driver.session_id, passed=False)
        #finally:
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()
        
    def wdselect(self):
        select = Select

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def get_page_src(self):
        return self.driver.page_source

if __name__ == "__self__":
    TestCase()