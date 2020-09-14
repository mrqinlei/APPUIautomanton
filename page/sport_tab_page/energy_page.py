# -*- coding: utf-8 -*-

from base.base_page import BasePage


class EnergyPage(BasePage):

    def get_energy_main(self):
        energy_temp = self.find_element_and_value("today_energy_num", "status_page_element")
        energy = energy_temp.split(" ")[1]
        return energy

    def get_energy_page_value(self):
        return self.find_element_and_value("energy_page_score", "status_page_element") + "千卡"

    def to_energy_page(self):
        self.find_element_and_click("today_energy_layout", "status_page_element")

    def click_week_energy_btn(self):
        self.find_element_and_click("week_energy","energy_page_element")

    def get_week_and_month_energy_time(self):
        return self.find_element_and_value("get_active_energy_time","energy_page_element")

    def click_month_energy_btn(self):
        self.find_element_and_click("month_energy","energy_page_element")
