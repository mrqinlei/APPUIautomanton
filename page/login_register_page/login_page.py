from base.base_page import BasePage


class LoginPage(BasePage):

    def login_by_phone(self, phone_number, pwd):
        self.find_element_and_sendKeys("username", "login_page_element", phone_number)
        self.find_element_and_sendKeys("password", "login_page_element", pwd)
        self.find_element_and_click("login_btn", "login_page_element")
        # self.find_element_and_click("advertisement_ball_cancel", "main_page_element")

    def get_sport_tab(self):
        return self.find_element("sport_tab", "main_page_element")

    def get_login_success_toast(self, toast_content):
        return self.find_toast_by_desc(toast_content)

    def to_xiaomi_login_page(self):
        self.find_element_and_click("xiaomi", "login_elements")

    def get_switch_btn(self):
        return self.find_element("switch_btn", "login_elements")

    def click_switch_btn(self):
        self.find_element_and_click("switch_btn", "login_elements")

    def edit_username_xiaomi(self, username):
        self.find_element_and_sendKeys("username_mi", "login_elements", username)

    def edit_pwd_xiaomi(self, pwd):
        self.find_element_and_sendKeys("password_mi", "login_elements", pwd)

    def click_login_xiaomi(self):
        self.find_element_and_click("login_btn_mi", "login_elements")
