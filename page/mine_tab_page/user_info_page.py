from base.base_page import BasePage

class UserInfoPage(BasePage):

    def get_nick_name_value(self):
        return self.find_elements_and_value("custom_info", "mine_page_element", 0)

    def to_edit_nick_name(self):
        self.find_elements_and_click("custom_key", "mine_page_element", 1)

    def nick_name_send_keys(self, nick_name):
        self.find_element_and_sendKeys("nick_name_edit", "mine_page_element", nick_name)

    def click_save_btn(self):
        self.find_element_and_click("save_btn", "mine_page_element")

    def to_edit_sex(self):
        self.find_elements_and_click("custom_key", "mine_page_element", 3)

    def get_sex_value(self):
        return self.find_element_and_value("sex_value", "mine_page_element")

    def chose_male_btn(self):
        self.find_element_and_click("male_btn", "mine_page_element")

    def chose_female_btn(self):
        self.find_element_and_click("female_btn", "mine_page_element")

    def get_height_value(self):
        return self.find_element_and_value("height_value", "mine_page_element")

    def to_edit_height(self):
        self.find_elements_and_click("custom_key", "mine_page_element", 5)

    def save_height(self):
        self.find_element_and_click("height_btn_save", "mine_page_element")

    def get_brief(self):
        return self.find_element_and_value("persion_brief_content", "mine_page_element")

    def to_edit_brief_page(self):
        self.find_elements_and_click("custom_key", "mine_page_element", 8)

    def edit_brief(self, context):
        self.find_element_and_sendKeys("edit_brief_content", "mine_page_element", context)

    def save_brief(self):
        self.find_element_and_click("right_btn", "mine_page_element")

    def to_image_page(self):
        self.find_element_and_click("right_photo","mine_page_element")

    def click_local_photo(self):
        self.find_element_and_click("select_local_photo","mine_page_element")

    def click_select_photo(self):
        self.find_element_and_click("select_photos","mine_page_element")

    def confirm_photo(self):
        self.find_element_and_click("confirm_photo","mine_page_element")

    def get_image_element(self):
        return self.find_element("right_photo","mine_page_element")

