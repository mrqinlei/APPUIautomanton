#-*- coding: utf-8 -*-

from base.base_page import BasePage

class TodayStepsPage(BasePage):

    def get_steps_today_page(self):
        return self.find_element_and_name("total_steps_num", "status_page_element")

    def click_share_btn(self):
        self.find_element_and_click("share_btn", "today_steps_page_element")

    def get_share_steps(self):
        return self.find_element_and_name("share_steps", "today_steps_page_element")

    def click_statistics_btn(self):
        self.find_element_and_click("statistics_btn", "today_steps_page_element")

    def click_statistics_day(self):
        self.find_element_and_click("statistics_day", "today_steps_page_element")

    def get_statistics_icon(self):
        return self.find_element("statistics_btn", "today_steps_page_element")



    def get_step_statistics(self):
        return self.find_element_and_value("statistics_text", "today_steps_page_element")

    def click_week_statistics(self):
        self.find_element_and_click("statistics_week","today_steps_page_element")

    def click_month_statistics(self):
        self.find_element_and_click("statistics_month","today_steps_page_element")

    def get_day_active_steps(self):
        return self.find_element_and_value("day_active_steps","today_steps_page_element")

    def get_day_active_time(self):
        return self.find_element_and_name("day_active_time","today_steps_page_element")

    def get_day_active_miles(self):
        return self.find_element_and_name("day_active_miles","today_steps_page_element")

    def get_day_use_calorie(self):
        return self.find_element_and_name("day_active_calorie","today_steps_page_element")

    def get_day_share_steps(self):
        return self.find_element_and_name("share_day_steps","today_steps_page_element")

    def day_share_back_btn(self):
        self.find_element_and_click("day_share_back_btn","today_steps_page_element")

    def get_day_share_times(self):
        return self.find_element_and_name("share_day_times","today_steps_page_element")

    def get_day_share_miles(self):
        return self.find_element_and_name("share_day_miles","today_steps_page_element")

    def get_day_share_carolie(self):
        return self.find_element_and_name("share_day_carolie","today_steps_page_element")

    def get_week_active_miles(self):
        return self.find_element_and_name("day_active_miles","today_steps_page_element")

    def get_week_active_carolie(self):
        return self.find_element_and_name("day_active_calorie","today_steps_page_element")

    def click_week_back_btn(self):
        self.find_element_and_click("week_share_back_btn","today_steps_page_element")

    def get_week_share_miles(self):
        return self.find_element_and_name("share_day_miles","today_steps_page_element")

    def get_week_share_carolie(self):
        return self.find_element_and_name("share_day_carolie","today_steps_page_element")

    def get_month_active_miles(self):
        return self.find_element_and_name("day_active_miles","today_steps_page_element")

    def get_month_active_carolie(self):
        return self.find_element_and_name("day_active_calorie","today_steps_page_element")

    def get_month_share_miles(self):
        return self.find_element_and_name("share_day_miles","today_steps_page_element")

    def get_month_share_carolie(self):
        return self.find_element_and_name("share_day_carolie","today_steps_page_element")









