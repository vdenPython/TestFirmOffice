


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd

        self.open_groups_page()

        wd.find_element_by_link_text("ДОБАВИТЬ ГРУППА").click()
        wd.find_element_by_id("id_name").clear()
        wd.find_element_by_id("id_name").send_keys(group.name)
        wd.find_element_by_name("_save").click()

        self.app.return_main_admin_django()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Группы").click()
