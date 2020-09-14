#-*- coding: utf-8 -*-

from base.base_page import BasePage

class SearchPage(BasePage):

    def click_search_edt(self):
        self.find_element_and_click("search_btn", "community_tab_case")
