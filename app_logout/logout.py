from xpath.xpath import XPATH
class logout:
    def __init__(self,driver):
        self.driver = driver
    def app_logout(self):
        try:
            print "LOG OUT APP IN PROGRESS...."
            elem = self.driver.selectXpath(XPATH.home_button,10)
            elem1 = self.driver.selectXpath(XPATH.user_image,10)
            elem2 = self.driver.selectXpath(XPATH.logout,10)
            elem3 = self.driver.selectXpath(XPATH.logout_popup,10)
            if elem3!=None:
                stat = self.driver.find_element_by_xpath(XPATH.login_button,10)
                if stat!=None:
                    print "Logout successful"
                    return True
                else:
                    print "Logout Failed"
                    return False
        except Exception as e:
            print "Exception occurred in app_logout method"
            return False
