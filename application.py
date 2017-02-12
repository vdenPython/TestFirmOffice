from selenium.webdriver.chrome.webdriver import WebDriver


class Application():

    def __init__(self):
        self.wd = WebDriver('/home/vden/PycharmProjects/ChromeDriver/chromedriver')
        self.wd.implicitly_wait(60)

    def logout_admin_django(self):
        wd = self.wd
        wd.find_element_by_link_text("ВЫЙТИ").click()

    def return_main_admin_django(self):
        wd = self.wd
        wd.find_element_by_link_text("Администрирование Django").click()

    def create_group(self, group):
        wd = self.wd

        self.open_groups_page()

        wd.find_element_by_link_text("ДОБАВИТЬ ГРУППА").click()
        wd.find_element_by_id("id_name").clear()
        wd.find_element_by_id("id_name").send_keys(group.name)
        wd.find_element_by_name("_save").click()

        self.return_main_admin_django()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Группы").click()

    def login_admin_django(self, username, password):
        wd = self.wd

        self.open_admin_django()

        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='submit-row']/input").click()

    def open_admin_django(self):
        wd = self.wd
        wd.get("http://127.0.0.1:8000/admin/")

    def destroy(self):
        self.wd.quit()


