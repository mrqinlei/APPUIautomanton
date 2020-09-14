# -*- coding: utf-8 -*-
from base.base_page import BasePage


class MySportsPage(BasePage):

    def get_my_sports_icon(self):
        return self.find_element_and_value("my_status_icon", "my_sports_page_element")

    def get_before_today_steps(self):
        return self.find_element_and_value("before_today_steps", "my_sports_page_element")

    def get_before_today_steps_miles(self):
        return self.find_element_and_value("before_today_steps_miles", "my_sports_page_element")

    def click_to_today_steps_page(self):
        self.find_element_and_click("before_today_steps", "my_sports_page_element")

    def get_after_today_steps(self):
        return self.find_element_and_name("after_today_steps", "my_sports_page_element")

    def get_after_today_steps_distance(self):
        return self.find_element_and_value("after_today_steps_miles","my_sports_page_element")

    def get_after_today_steps_carol(self):
        return self.find_element_and_value("after_today_carol","my_sports_page_element")

    def get_before_today_sports_miles(self):
        return self.find_element_and_value("before_today_sports_miles", "my_sports_page_element")

    def click_to_today_sports_miles_page(self):
        self.find_element_and_click("before_today_sports_miles", "my_sports_page_element")

    def click_count_by_week(self):
        self.find_element_and_click("click_count_by_week","my_sports_page_element")

    def get_after_today_sports_miles(self):
        return self.find_element_and_value("after_today_sports_miles", "my_sports_page_element")

    def get_before_today_energy(self):
        return self.find_element_and_value("before_today_energy", "my_sports_page_element")

    def click_to_today_energy_page(self):
        self.find_element_and_click("before_today_energy", "my_sports_page_element")

    def get_after_today_energy(self):
        return self.find_element_and_value("after_today_energy", "my_sports_page_element")

    def get_before_goal(self):
        return self.find_element_and_value("before_goal_value", "my_sports_page_element")

    def click_to_goal_page(self):
        self.find_element_and_click("before_goal_value", "my_sports_page_element")

    def get_after_goal(self):
        return self.find_element_and_name("after_goal_value", "my_sports_page_element")

    def click_goal_back_to_my_sports(self):
        self.find_element_and_click("goal_page_back_to_my_sports_btn", "my_sports_page_element")
