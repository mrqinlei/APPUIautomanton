# -*- coding: utf-8 -*-

from base.base_page import BasePage


class MyEquipmentPage(BasePage):

    def click_my_bus_card(self):
        self.find_element_and_click("my_bus_card", "mine_equipment_element")

    def get_bus_card_detail(self):
        return self.find_element_and_value("my_bus_card_detail", "mine_equipment_element")
