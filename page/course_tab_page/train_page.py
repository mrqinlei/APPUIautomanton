# -*- coding: utf-8 -*-

from base.base_page import BasePage


class CourseTrainPage(BasePage):
    def click_join_train(self):
        self.find_element_and_click("into_train_page","course_page_element")

    def click_select_train_target(self):
        self.find_element_and_click("train_target","course_page_element")

    def click_next_step(self):
        self.find_element_and_click("click_next_step","course_page_element")

    def click_select_train_level(self):
        self.find_element_and_click("train_target","course_page_element")

    def click_select_start_date(self):
        self.find_element_and_click("start_date","course_page_element")

    def click_join_train_btn(self):
        self.find_element_and_click("join_train_btn","course_page_element")

    def click_start_train(self):
        self.find_element_and_click("start_train","course_page_element")

    def click_download_all_video(self):
        self.find_element_and_click("download_all_video","course_page_element")

    def click_download_today_video(self):
        self.find_element_and_click("download_today_video","course_page_element")

    def judge_already_download_video(self):
        return self.find_element("download_today_video","course_page_element")

    def touch_video(self):
        self.find_element_and_click("touch_video","course_page_element")

    def click_close_video_btn(self):
        self.find_element_and_click("video_close","course_page_element")

    def confirm_close_video(self):
        self.find_element_and_click("video_confirm_close","course_page_element")

    def video_play_surface_judge(self):
        return self.find_element("video_play_surface","course_page_element")

    def click_more_btn(self):
        self.find_element_and_click("more_btn","course_page_element")

    def get_more_btn(self):
        return self.find_element("more_btn","course_page_element")

    def click_exit_train(self):
        self.find_element_and_click("exit_train_btn","course_page_element")

    def click_confirm_exit_train_btn(self):
        self.find_element_and_click("confirm_btn","course_page_element")

    def get_train_name(self):
        return self.find_element_and_value("get_train_name","course_page_element")

    def click_continue_train(self):
        self.find_element_and_click("continue_train","course_page_element")

    def judge_if_already_join_train(self):
        return self.find_element("continue_train","course_page_element")

    def get_exit_train_result_element(self):
        return self.find_element("into_train_page","course_page_element")


