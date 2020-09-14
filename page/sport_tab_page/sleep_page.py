#-*- coding: utf-8 -*-

from base.base_page import BasePage

class SleepPage(BasePage):

    def get_sleep(self):
        return self.find_element_and_value("sleep", "sleep_page_element")

    def click_share_btn(self):
        self.find_element_and_click("share_btn", "sleep_page_element")

    def get_sleep_share(self):
        return self.find_element_and_value("sleep_time", "sleep_page_element")

    def get_sleep_info_value(self):
        return self.find_element_and_name("sleep_info_value", "sleep_page_element")

    def get_sleep_share_value(self):
        return self.find_element_and_name("sleep_share_value", "sleep_page_element")

    def get_start_time(self):
        return self.find_element_and_value("start_time", "sleep_page_element")

    def get_stop_time(self):
        return self.find_element_and_value("stop_time", "sleep_page_element")

    def click_edit_btn(self):
        self.find_element_and_click("edit_btn", "sleep_page_element")

    def get_start_edit(self):
        return self.find_element_and_value("start_edit_text", "sleep_page_element")

    def get_stop_edit(self):
        return self.find_element_and_value("stop_edit_text", "sleep_page_element")

    def click_start_edit(self):
        self.find_element_and_click("start_edit_layout", "sleep_page_element")

    def click_stop_edit(self):
        self.find_element_and_click("stop_edit_layout", "sleep_page_element")

    def click_save_btn(self):
        self.find_element_and_click("save_btn", "sleep_page_element")

    def get_edit_icon(self):
        return self.find_element("edit_btn", "sleep_page_element")



