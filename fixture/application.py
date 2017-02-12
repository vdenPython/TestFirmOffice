from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application():

    def __init__(self):
        self.wd = WebDriver('/home/vden/PycharmProjects/ChromeDriver/chromedriver')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group =GroupHelper(self)

    def return_main_admin_django(self):
        wd = self.wd
        wd.find_element_by_link_text("Администрирование Django").click()

    def open_admin_django(self):
        wd = self.wd
        wd.get("http://127.0.0.1:8000/admin/")

    def destroy(self):
        self.wd.quit()


