# -*- coding: utf-8 -*-

from base.base_page import BasePage


class CoursePage(BasePage):

    def get_first_course_name(self):
        return self.find_element_and_value("first_course_name", "mine_course_page_element")

    def get_course_name(self):
        return self.find_element_and_value("course_page_name", "mine_course_page_element")

    def to_first_course_page(self):
        self.find_element_and_click("first_course_layout", "mine_course_page_element")

    def to_add_course_list(self):
        self.find_element_and_click("add_course_btn", "mine_course_page_element")

    def click_to_my_course(self):
        self.find_element_and_click("mine_course", "mine_page_element")

    def get_first_course_list_name(self):
        return self.find_element_and_value("list_course_first_name", "mine_course_page_element")

    def get_first_course_list_name_2(self):
        return self.find_element_and_value("list_course_first_name_2", "mine_course_page_element")

    def to_first_course_list(self):
        self.find_element_and_click("list_course_first", "mine_course_page_element")

    def add_coursec_btn(self):
        self.find_element_and_click("join_course_btn", "mine_course_page_element")

    def get_course_info(self):
        return self.find_element_and_value("join_course_btn", "mine_course_page_element")

    def back_to_course_list(self):
        self.find_element_and_click("back_to_course_list", "mine_course_page_element")

    def back_to_mine_course(self):
        self.find_element_and_click("back_to_mine_course", "mine_course_page_element")

    def click_run_tab(self):
        self.find_element_and_click("run_tab", "mine_course_page_element")

    def click_all_tab(self):
        self.find_element_and_click("all_tab", "mine_course_page_element")

    def click_yoga_tab(self):
        self.find_element_and_click("yoga_tab", "mine_course_page_element")

    def find_free_course(self):
        return self.find_element_to_element("Free")

    def click_free_course_label(self):
        self.find_element_and_click("free_course", "mine_course_page_element")

    def get_add_course_icon(self):
        return self.find_element("add_course_btn", "mine_course_page_element")

    def get_buy_course_info(self):
        return self.find_element_and_value("buy_course_btn", "mine_course_page_element")

    def click_to_pay_page(self):
        self.find_element_and_click("buy_course_btn", "mine_course_page_element")

    def get_confirm_pay_btn(self):
        return self.find_element_and_value("confirm_pay_btn", "mine_course_page_element")

    def find_quality_goods(self):
        return self.find_element_to_element("精品")

    def click_quality_goods_label(self):
        self.find_element_and_click("boutique_course", "mine_course_page_element")

    def click_to_course_list(self):
        self.find_element_and_click("course_list_btn", "mine_course_page_element")

    def click_to_watch_video(self):
        self.find_element_and_click("course_video_cover", "mine_course_page_element")

    def click_to_pause_video(self):
        self.find_element_and_click("video_pause_btn", "mine_course_page_element")

    def get_video_play_element(self):
        return self.find_element("video_play", "mine_course_page_element")

    def click_to_exit_video(self):
        self.find_element_and_click("video_exit_btn", "mine_course_page_element")

    def click_feedback(self):
        self.find_element_and_click("feed_back_btn", "mine_course_page_element")

    def click_more_btn(self):
        self.find_element_and_click("more_btn", "mine_course_page_element")

    def click_exit_course_btn(self):
        self.find_element_and_click("exit_course", "mine_course_page_element")
