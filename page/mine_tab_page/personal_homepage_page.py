#-*- coding: utf-8 -*-

from base.base_page import BasePage

class PersonalHomepagePage(BasePage):

    # def get_my_dynamic_counts(self):
    #     return self.find_element_and_value("mine_dynamic", "mine_page_element")
    #
    # def to_my_zone(self):
    #     self.find_element_and_click("mine_dynamic", "mine_page_element")
    #
    # def get_my_dynamic_num(self):
    #     return self.find_element_and_value("dynamic_counts", "mine_page_element")

    def click_person_profile(self):
        self.find_element_and_click("edit_profile_btn", "personal_homepage_element")

    def click_care_btn(self):
        self.find_element_and_click("care_btn", "personal_homepage_element")

    def click_fans_btn(self):
        self.find_element_and_click("fans_btn", "personal_homepage_element")

    def to_medal_page(self):
        self.find_element_and_click("medal_more_btn", "personal_homepage_element")

    def get_title(self):
        return self.find_element_and_value("title", "personal_homepage_element")

    def to_diary_page(self):
        self.find_element_and_click("my_diary", "personal_homepage_element")

    def to_post_page(self):
        self.find_element_and_click("first_post", "personal_homepage_element")

    def get_first_post_name(self):
        return self.find_element_and_value("first_post_nick_name", "personal_homepage_element")

    def get_publisher_name(self):
        return self.find_element_and_value("publisher_name", "personal_homepage_element")

    def click_video_tab(self):
        self.find_element_and_click("video_tab", "personal_homepage_element")

    def get_edit_profile_icon(self):
        return self.find_element("edit_profile_btn", "personal_homepage_element")

