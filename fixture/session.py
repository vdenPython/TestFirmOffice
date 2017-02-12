


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_admin_django(self, username, password):
        wd = self.app.wd

        self.app.open_admin_django()

        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='submit-row']/input").click()

    def logout_admin_django(self):
        wd = self.app.wd
        wd.find_element_by_link_text("ВЫЙТИ").click()

