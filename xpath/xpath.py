from selenium.webdriver.common.by import By
from driver.driver import appiumdriver
class XPATH():
    #remotedrive = appiumdriver()
    #driver = remotedrive.driver
    login_button = '//*[contains(@resource-id,"com.ebay.mobile:id/button_sign_in")]'
    user_name = '//*[contains(@resource-id,"com.ebay.mobile:id/edit_text_username")]'
    password = '//*[contains(@resource-id,"com.ebay.mobile:id/edit_text_password")]'
    sign_in_button = '//*[contains(@resource-id,"com.ebay.mobile:id/button_sign_in")]'
    no_thanks_opt = '//*[contains(@resource-id,"com.ebay.mobile:id/button_google_deny")]'
    home_search_bar = '//*[contains(@resource-id,"search_box")]'
    search_bar_after_click = '//*[contains(@resource-id,"search_src_text")]'
    option = '//*[contains(@resource-id,"com.ebay.mobile:id/text)]'
    suggest_list = (By.XPATH,'//android.widget.ListView/android.widget.RelativeLayout[1]')
    pop_up = '//*[contains(@resource-id,"popup_container")]'
    first_search_result = (By.XPATH,'//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]')
    buy_it_now = '//*[contains(@resource-id,"button_bin")]'
    category_selection = '//*[contains(@resource-id,"spinner_selection_option")]'
    category_option = (By.XPATH,'//android.widget.ListView/android.widget.FrameLayout[2]')
    buy_it_now_after = '//*[contains(@resource-id,"button_bin_buybar")]'
    home_button = '//*[contains(@resource-id,"com.ebay.mobile:id/home")]'
    user_image = '//*[contains(@resource-id,"com.ebay.mobile:id/image_user_profile")]'
    logout = '//*[contains(@text,"Sign out")]'
    logout_popup = '//*[contains(@text,"OK")]'






    def selectXpath(self,xpath, waitSec=10):
        try:
            print "Selecting XPath: {}".format(str(xpath))
            aElem = self.driver.find_element_by_xpath(xpath)
            if (aElem != None):
                aElem.click()
                return aElem
        except:
            return None


