#-*- coding: utf-8 -*-

from base.base_page import BasePage

class CollectPage(BasePage):

    def to_first_post_page(self):
        self.find_element_and_click("first_post", "mine_collect_page_element")

    def get_first_post_name(self):
        return self.find_element_and_value("first_post_nick_name", "mine_collect_page_element")

    def get_publisher_name(self):
        return self.find_element_and_value("publisher_name", "mine_collect_page_element")

    def to_course_tab(self):
        self.find_element_and_click("course_tab", "mine_collect_page_element")

    def get_first_course_name(self):
        return self.find_element_and_value("first_course_post_name", "mine_collect_page_element")

    def to_first_course_page(self):
        self.find_element_and_click("first_course_post", "mine_collect_page_element")

    def get_course_name(self):
        return self.find_element_and_value("course_page_name", "mine_collect_page_element")

    def get_my_collect_icon(self):
        return self.find_element_and_value("title", "mine_page_element")

    def get_course_tab(self):
        return self.find_element("course_tab", "mine_collect_page_element")


