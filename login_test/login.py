from xpath.xpath import XPATH
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from driver.driver import appiumdriver
import time

class login:
    def __init__(self,driver):
        self.driver = driver
        print self.driver


    def user_login(self,user,pwd,app):
        try:
            if app == 'ebay':
                print "LOG IN TO EBAY APPLICATION IS IN PROGRESS.."
                time.sleep(10)
                status = self.driver.selectXpath(XPATH.login_button,20)
                print status
                if status!=None:
                    elem = self.driver.selectXpath(XPATH.user_name,10)
                    elem.send_keys(user)
                    elem1 = self.driver.selectXpath(XPATH.password,10)
                    elem1.send_keys(pwd)
                    if elem and elem1!=None:
                        stat = self.driver.selectXpath(XPATH.sign_in_button,10)
                        time.sleep(10)
                        stat1 = self.driver.selectXpath(XPATH.no_thanks_opt,10)
                        if stat and stat1!=None:
                            print "Logged in successfully"
                            return True
                        else:
                            print "Login error"
                            return False
                    else:
                        print "User name or password not entered"
                        return False

                else:
                    print "Sign in button click failed"
                    return False
            elif app =='amazon':
                pass
            elif app =='flipkart':
                pass
            else:
                print "App type not given"
                return False


        except Exception as e:
            print('exception raised in login_ebay function ' )
            print (e)
            return False

    def search_product(self,productname):
        if productname:
            elem = self.driver.selectXpath(XPATH.home_search_bar,10)
            print elem
            if elem!=None:
                self.driver.send_keys(XPATH.search_bar_after_click, productname)
                time.sleep(10)
                #elem1 = self.driver.selectXpath(XPATH.search_bar_after_click,20)
                elem2 = self.driver.selectXpath(XPATH.suggest_list,20)
                elem3 = self.driver.selectXpath(XPATH.pop_up,10)
                elem4 = self.driver.selectXpath(XPATH.first_search_result,10)
        elem5 = self.driver.selectXpath(XPATH.buy_it_now,10)
        elem6 = self.driver.selectXpath(XPATH.category_selection,10)
        elem6 = self.driver.selectXpath(XPATH.category_option,10)
        elem7 = self.driver.selectXpath(XPATH.buy_it_now_after,10)
        return True
        pass


    def findXpath(self, xpath, waitSec=1):
        try:
            print "Finding XPath: {}".format(str(xpath))
            return self.driver.find_element_by_xpath(xpath)
        except:
            return None

