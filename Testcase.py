import os
import unittest
import time
from login_test.login import login
from search_product.search_prod import Searchproduct
from app_logout.logout import logout
from driver.driver import appiumdriver
user = "aravindarjun48@gmail.com"
pwd = "aravindarjun10$"
html_pass = '<b style="color:green">PASS</b>'
html_fail = '<b style="color:red">FAIL</b>'
class Ebayapplication(unittest.TestCase):
    "Class to run tests on the Ebay app"

    def testcase_test(self):
        "Setup for the test"
        try:
            self.mydriver = appiumdriver()
            self.login_obj = login(self.mydriver)
            status = self.login_obj.user_login(user, pwd, "ebay")
            if status:
                print "Login completed successfully",html_pass

            else:
                print "Login operation failed",html_fail
            self.product_obj = Searchproduct(self.mydriver)
            msg = self.product_obj.search_product("Moto G5 plus")
            if msg:
                print "Product searched Successfully",html_pass
            else:
                print "Product search fail",html_fail
            self.logout_obj = logout(self.mydriver)
            msg2 = self.logout_obj.app_logout()
            if msg2:
                print "App logged out successfully",html_pass
                return True
            else:
                print "App log out failed",html_fail
                return False
        except Exception as e:
            print "Exception occured in Testcase test block",html_fail
            return False

    def tearDown(self):
        "Tear down the test"
        pass


# ---START OF SCRIPT
if __name__ == '__main__':
    unittest.main()