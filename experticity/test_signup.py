from Page_Object import Experticity as EX
import os
import utils
import time
import uuid
from datetime import datetime

FILE_PATH = os.path.abspath(os.path.dirname(__file__))
CFG =utils.parse_config(FILE_PATH + "/config.ini")
STR_FMT = "%Y-%m-%d.%H-%M-%S"


class Test_Signup(EX):


    def test_signup(self):
        browser = CFG.get("signup", "browser")
        url = CFG.get("signup", "url")
        guid = uuid.uuid4()
        date = datetime.now().strftime(STR_FMT)
        email = "qa.{browser}.{date}@experticity.com".format(browser=browser, date=date)
        first_name = CFG.get("signup", "first_name")
        last_name = CFG.get("signup", "last_name")
        username = "user{guid}".format(guid=guid)
        password = CFG.get("signup", "password")
        position = CFG.get("signup", "position")
        hiredate = CFG.get("signup", "hire_date")
        referral = CFG.get("signup", "referral")
        store = CFG.get("signup", "store")
        zip = CFG.get("signup", "zip")



        EX.homepage(self, url)
        print("got to form ok")
        EX.email(self, email)
        print "setting this unique email: ", email
        EX.first_name(self, first_name)
        print("set first name")
        EX.last_name(self, last_name)
        print("set last name")
        EX.user_name(self, username)
        print "set unique username: ",username
        EX.password(self, password)
        print "setting password to: ", password
        EX.confirm(self, password)
        EX.position(self, position)
        print "set position to: ", position
        EX.hire_date(self, hiredate)
        print "set hire date to: ", hiredate
        time.sleep(1)
        EX.referral(self, referral)
        print"set referral type to ", referral
        EX.click_next(self)
        print("form completed without error")
        time.sleep(3)
        EX.search_store(self, store=store)
        print "found store ", store
        time.sleep(1)
        EX.select_store(self, store=store)
        print "selected store: ", store
        EX.submit_form(self)
        time.sleep(1)
        print("submitted confirmation form")
        EX.final_submit(self)
        print("submitted final form")
        EX.assert_expertise(self)