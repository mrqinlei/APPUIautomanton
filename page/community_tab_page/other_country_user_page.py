#-*- coding: utf-8 -*-

from base.base_page import BasePage

class OtherCountryUserPage(BasePage):

    def search_friends_element(self):
        return self.find_element("foreign_friends","main_page_element")

    def search_classes_tab_element(self):
        return self.find_element("classes_tab","main_page_element")

    def search_descovery_tab_element(self):
        return self.find_element("descovery_tab","main_page_element")

    def get_foreign_workout_icon(self):
        return self.find_element("foreign_workout","main_page_element")

    def login_by_phone(self, phone_number, pwd):
        self.find_element_and_sendKeys("username", "login_page_element", phone_number)
        self.find_element_and_sendKeys("password", "login_page_element", pwd)
        self.find_element_and_click("login_btn", "login_page_element")

    def click_not_xiaomi_account_login(self):
        self.find_element_and_click("judge_xiaomi_account_login","main_page_element")

    def get_judge_xiaomi_account(self):
        return self.find_element("judge_xiaomi_account_login","main_page_element")

    def get_not_chinese_account_sports_icon(self):
        return self.find_element("not_chinese_account_sports","main_page_element")

    def get_not_chinese_account_friends_icon(self):
        return self.find_element("not_chinese_account_friends","main_page_element")

    def get_not_chinese_account_mine_icon(self):
        return self.find_element("not_chinese_account_mine","main_page_element")

    def click_to_not_chinese_mine_page(self):
        self.find_element_and_click("not_chinese_account_mine","main_page_element")

    def swipe_to_settings_element(self):
        return self.swipe_on("up")

    def click_settings_btn(self):
        self.find_element_and_click("not_chinese_account_settings_btn","main_page_element")

    def click_logout_btn(self):
        self.find_element_and_click("not_chinese_account_logout_btn","main_page_element")

    def click_confirm_exit_account(self):
        self.find_element_and_click("confirm_exit_account_btn","main_page_element")

    def click_confirm_exit(self):
        self.find_element_and_click("confirm_exit_account_btn","main_page_element")

    def get_discover_tab(self):
        return self.find_element("descovery_tab","main_page_element")

    def judge_chinese_account_if_login(self):
        return self.find_element("sport_tab","main_page_element")

    def judge_not_chinese_account_if_login(self):
        return self.find_element("not_chinese_account_sports","main_page_element")

    def click_to_mine_tab(self):
        self.find_element_and_click("mine_tab","main_page_element")

    def click_not_have_band_got_it(self):
        self.find_element_and_click("got_it","main_page_element")

    def judge_if_have_not_band(self):
        return self.find_element("got_it","main_page_element")




