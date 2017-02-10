# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver('/home/vden/PycharmProjects/ChromeDriver/chromedriver')
        self.wd.implicitly_wait(60)
    
    def test_test_add_group(self):
        wd = self.wd
        self.open_admin_django(wd)
        self.login_admin_django(wd, username= "test", password= "test12345")
        self.open_groups_page(wd)
        self.create_group(wd, name= "test1")
        self.return_main_admin_django(wd)
        self.logout_admin_django(wd)

    def logout_admin_django(self, wd):
        wd.find_element_by_link_text("ВЫЙТИ").click()

    def return_main_admin_django(self, wd):
        wd.find_element_by_link_text("Администрирование Django").click()

    def create_group(self, wd, name):
        wd.find_element_by_link_text("ДОБАВИТЬ ГРУППА").click()
        wd.find_element_by_id("id_name").clear()
        wd.find_element_by_id("id_name").send_keys(name)
        wd.find_element_by_name("_save").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("Группы").click()

    def login_admin_django(self, wd, username, password):
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='submit-row']/input").click()

    def open_admin_django(self, wd):
        wd.get("http://127.0.0.1:8000/admin/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
