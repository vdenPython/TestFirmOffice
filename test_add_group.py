# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver('/home/vden/PycharmProjects/ChromeDriver/chromedriver')
        #self.wd = WebDriver('/home/vden/PycharmProjects/geckodriver')
        self.wd.implicitly_wait(60)
    
    def test_test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://127.0.0.1:8000/admin/")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").send_keys("\\undefined")
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys("test")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys("test12345")
        wd.find_element_by_xpath("//div[@class='submit-row']/input").click()
        wd.find_element_by_link_text("ВЫЙТИ").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
