#-*- coding: utf-8 -*-

from base.base_page import BasePage

class MineSportPage(BasePage):

    def get_steps_mine_page(self):
        steps_nums = self.find_element_and_value("today_steps_num", "status_page_element")
        steps = steps_nums.split(" ")[1]
        return steps

    def to_today_steps_page(self):
        self.find_element_and_click("today_steps_layout", "status_page_element")

    def get_steps_today_page(self):
        steps_nums = self.find_element_and_name("total_steps_num", "status_page_element")
        steps_temp = steps_nums.split(",")[0]
        steps = steps_temp[1:]
        return steps

    def get_energy_main(self):
        energy_temp = self.find_element_and_value("today_energy_num", "status_page_element")
        energy = energy_temp.split(" ")[1]
        return energy

    def to_energy_page(self):
        self.find_element_and_click("today_energy_layout", "status_page_element")

    def get_energy_page_value(self):
        return self.find_element_and_value("energy_page_score", "status_page_element") + "千卡"

    def get_reach_days_main(self):
        reach_days_temp = self.find_element_and_value("reach_days_num", "status_page_element")
        reach_days = reach_days_temp.split(" ")[1]
        return reach_days

    def to_reach_days_page(self):
        self.find_element_and_click("reach_layout", "status_page_element")

    def get_reach_days_value(self):
        reach_days_temp = self.find_element_and_name("reach_days", "status_page_element")
        reach_days = reach_days_temp.split(",")[0]
        return reach_days[1:]

    def to_today_sport_page(self):
        self.find_element_and_click("today_sport_layout", "status_page_element")

    def get_today_sport_title(self):
        return self.find_element_and_value("total_sport", "status_page_element")

    def get_today_all_sport_run_mile(self):
        return self.find_element_and_value("all_sports_run_mile","status_page_element")

