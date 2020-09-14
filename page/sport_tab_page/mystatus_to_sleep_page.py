# -*- coding: utf-8 -*-

from base.base_page import BasePage


class MyStatusSleepPage(BasePage):

    def get_sleep_score(self):
        return self.find_element_and_value("sleep_score", "sleep_page_element")

    def click_day_btn(self):
        self.find_element_and_click("sleep_day_btn", "sleep_page_element")

    def click_week_btn(self):
        self.find_element_and_click("sleep_week_btn", "sleep_page_element")

    def get_click_result(self):
        return self.find_element_and_value("get_click_view_result", "sleep_page_element")

    def click_month_btn(self):
        self.find_element_and_click("sleep_month_btn", "sleep_page_element")

    def click_year_btn(self):
        self.find_element_and_click("sleep_year_btn", "sleep_page_element")

    def get_edit_icon(self):
        return self.find_element("edit_btn", "sleep_page_element")

    def get_sleep(self):
        return self.find_element_and_value("share_btn", "sleep_page_element")
