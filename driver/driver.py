from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
class appiumdriver:
    progress_bar = (By.ID, 'progress_bar')
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.ebay.mobile'
        desired_caps['appActivity'] = 'com.ebay.mobile.activities.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        logging.getLogger().setLevel(logging.INFO)
        self.log = logging.getLogger(__name__)

    def selectXpath(self, xpath, waitSec=10):
        try:
            print "Selecting XPath: {}".format(str(xpath))
            aElem = self.driver.find_element_by_xpath(xpath)
            if (aElem != None):
                aElem.click()
                return aElem
        except:
            return None


    def send_keys(self, locator, key_inputs):
        """
        Typing keys at input locator
        :param locator:
        :param key_inputs:
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)).send_keys(key_inputs)
        except Exception as e:
            print "Exception in send_keys"

    def wait_for_loading(self):
        """

        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.progress_bar))
        except Exception as e:
            self.log.info("Exception while waiting for the progress bar to disappear " + str(e))


    def click(self, locator, wait_time=10):
        """

        :param locator:
        :param wait_time:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator))
            element.click()
            self.wait_for_loading()
        except Exception as e:
            self.log.info("Exception while clicking the element " + str(e))
