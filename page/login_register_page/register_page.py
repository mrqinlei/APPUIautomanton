from base.base_page import BasePage


class RegisterPage(BasePage):


    def register_by_phoen(self):
        self.find_element_and_click("register_btn", "login_page_element")
