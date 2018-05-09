from xpath.xpath import XPATH
from appium import webdriver
from selenium import webdriver
from appium.webdriver.webdriver import WebDriver as wd
from appium.webdriver.common.touch_action import TouchAction
import time
DEFAUL_WAIT_TIME = 20
class Searchproduct:
    def __init__(self,driver,objsuite):
        self.objsuite = objsuite
        self.driver = driver
        #self.webdriv = webdriv
    def search_product(self,productname):
        """
            :Step 1: Click on search bar
            :Step 2: Send the input product to be searched
            :Step 3: Check whether source text exists in search bar
            :Step 4: Click on the first option in suggestion list
            :Step 5: Tap on the screen to avoid pop up
            :Step 6: Click on first search result
            :Step 7: Click on purchase it now
            :return: NONE
                """
        try:
            if productname:
                elem = self.driver.custom_driver_wait(XPATH.home_search_bar,DEFAUL_WAIT_TIME)
                print elem
                if elem!=None:
                    elem.send_keys(productname)
                    elem1 = self.driver.custom_driver_wait(XPATH.search_bar_after_click)
                    #time.sleep(10)
                    elem2 = self.driver.click(XPATH.suggest_list,DEFAUL_WAIT_TIME)
                    elem3 = self.driver.selectXpath(XPATH.pop_up,DEFAUL_WAIT_TIME)
                    elem4 = self.driver.click(XPATH.first_search_result,DEFAUL_WAIT_TIME)
            elem5 = self.driver.selectXpath(XPATH.buy_it_now,DEFAUL_WAIT_TIME)
            if elem5!=None:
                print "Product purchased successfully"
                return True
            else:
                print "Failed to purchase the product"
                return False
        except Exception as e:
            print "Exception occured in Search product block"
            return False