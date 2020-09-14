# -*- coding: utf-8 -*-

from base.base_page import BasePage


class WeightPage(BasePage):

    def get_weight_info(self):
        return self.find_element_and_value("weight_info", "weight_page_element")

    def click_weight(self):
        self.find_element_and_click("weight_layout", "weight_page_element")

    def get_weight_data(self):
        return self.find_element_and_value("weight_data", "weight_page_element")
