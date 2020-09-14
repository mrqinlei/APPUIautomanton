# -*- coding: utf-8 -*-

from base.base_page import BasePage


class HeartRatePage(BasePage):

    def get_heart_rate_info(self):
        return self.find_element_and_value("heart_rate_times", "heart_rate_page_element")

    def click_heart_rate(self):
        self.find_element_and_click("heart_rate_layout", "heart_rate_page_element")

    def get_hr_data(self):
        return self.find_element_and_value("hr_data", "heart_rate_page_element")
