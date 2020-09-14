#-*- coding: utf-8 -*-

from base.base_page import BasePage

class MyStatusPage(BasePage):

    def get_my_status_icon(self):
        return self.find_element("my_status_icon","my_status_page_element")

    def find_before_pai_element(self):  #此方法为滑动查找元素 用例里未用到
        self.find_element_to_element(to_element_id="all_before_pai_value")

    def find_pai_guide_element(self):
        return self.find_element("pai_guide_layout","my_status_page_element")

    def get_before_pai_value(self):
        return self.find_element_and_value("all_before_pai_value","my_status_page_element")

    def get_today_pai_value(self):
        return self.find_element_and_value("today_before_pai_value","my_status_page_element")

    def click_to_pai_page(self):
        self.find_element_and_click("all_before_pai_value","my_status_page_element")

    def get_after_all_pai_value(self):
        return self.find_element_and_value("all_after_pai_value","my_status_page_element")

    def get_after_today_pai_value(self):
        return self.find_element_and_value("today_after_pai_value","my_status_page_element")

    def get_before_recent_press(self):
        return self.find_element_and_value("before_recent_press_value","my_status_page_element")

    def click_to_press_page(self):
        self.find_element_and_click("before_recent_press_value","my_status_page_element")

    def get_after_recent_press(self):
        return self.find_element_and_value("after_recent_press_value","my_status_page_element")

    def get_before_heart_rate(self):
        return self.find_element_and_value("before_heart_rate_value","my_status_page_element")

    def click_to_heart_rate_page(self):
        self.find_element_and_click("before_heart_rate_value","my_status_page_element")

    def get_after_heart_rate(self):
        return self.find_element_and_value("after_heart_rate_value","my_status_page_element")

    def swipe_to_bottle(self):
        self.swipe_on("up")

    def swipe_to_half(self):
        self.swipe_on("up_middle")

    def find_before_last_sleep_element(self):
        return self.find_element_to_element(to_element_id="深睡")

    def find_before_weight_value(self):
        self.find_element_to_element(to_element_id="体重")

    def find_body_fat_element(self):
        self.find_element_to_element(to_element_id="身体指数")

    def find_balance_element(self):
        self.find_element_to_element(to_element_id="平衡性")

    def get_before_weight_value(self):
        return self.find_element_and_value("before_weight_value","my_status_page_element")

    def click_to_weight_page(self):
        self.find_element_and_click("before_weight_value","my_status_page_element")

    def get_after_weight_value(self):
        return self.find_element_and_value("after_weight_value","my_status_page_element")

    def get_before_sleep_time(self):
        return self.find_element_and_value("before_sleep_time","my_status_page_element")

    def click_to_sleep_page(self):
        self.find_element_and_click("before_sleep_time","my_status_page_element")

    def get_after_sleep_time(self):
        return self.find_element_and_value("after_sleep_time","my_status_page_element")

    def get_before_body_fat(self):
        return self.find_element_and_value("before_body_fat","my_status_page_element")

    def click_to_body_fat_page(self):
        self.find_element_and_click("before_body_fat","my_status_page_element")

    def get_after_body_fat(self):
        return self.find_element_and_name("after_body_fat","my_status_page_element")

    def get_before_balance(self):
        return self.find_element_and_value("before_balance","my_status_page_element")

    def click_to_balance_page(self):
        self.find_element_and_click("before_balance","my_status_page_element")

    def get_after_balance(self):
        return self.find_element_and_value("after_balance","my_status_page_element")

    def click_to_little_sleep(self):
        self.find_element_and_click("my_little_sleep","my_status_page_element")

    def get_before_little_sleep_time(self):
        return self.find_element_and_value("my_little_sleep_time","my_status_page_element")

    def get_after_little_sleep_time(self):
        return self.find_element_and_value("my_little_sleep_day_time","my_status_page_element")




