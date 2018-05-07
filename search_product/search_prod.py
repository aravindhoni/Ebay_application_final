from xpath.xpath import XPATH
import time
class Searchproduct:
    def __init__(self,driver):
        self.driver = driver
    def search_product(self,productname):
        try:
            if productname:
                time.sleep(10)
                elem = self.driver.selectXpath(XPATH.home_search_bar,10)
                print elem
                if elem!=None:
                    elem.send_keys(productname)
                    elem1 = self.driver.selectXpath(XPATH.search_bar_after_click,10)
                    time.sleep(10)
                    elem2 = self.driver.click(XPATH.suggest_list,20)
                    time.sleep(5)
                    elem3 = self.driver.selectXpath(XPATH.pop_up,10)
                    elem4 = self.driver.click(XPATH.first_search_result,10)
            elem5 = self.driver.selectXpath(XPATH.buy_it_now,10)
            if elem5!=None:
                print "Product purchased successfully"
                return True
            else:
                print "Failed to purchase the product"
                return False
        except Exception as e:
            print "Exception occured in Search product block"
            return False







        #     self.base_page.click(self.home_search_bar)
        #     self.base_page.send_keys(self.search_bar_after_click, productname)
        #     self.base_page.click(self.suggest_list)
        #     self.base_page.click(self.pop_up)
        #     self.base_page.click(self.first_search_result)
        # self.base_page.click(self.buy_it_now)
        # self.base_page.click(self.category_selection)
        # self.base_page.click(self.category_option)
        # self.base_page.click(self.buy_it_now_after)
        pass


    def selectXpath(self, xpath, waitSec=10):
        try:
            print "Selecting XPath: {}".format(str(xpath))
            aElem = self.driver.find_element_by_xpath(xpath)
            if (aElem != None):
                aElem.click()
                return aElem
        except:
            return None