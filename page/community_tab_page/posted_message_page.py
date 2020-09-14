# -*- coding: utf-8 -*-

from base.base_page import BasePage


class PostedMessagePage(BasePage):

    def get_community_icon(self):
        return self.find_element("community_tab", "main_page_element")

    def to_publish_post(self):
        self.find_element_and_click("to_post_btn", "community_page_element")

    def to_select_post_btn(self):
        self.find_element_and_click("post_btn","community_page_element")

    def judge_have_diary_authority(self):
        return self.find_element("post_btn","community_page_element")

    def to_select_photo_btn(self):
        self.find_element_and_click("select_photo", "community_page_element")

    def click_next_btn(self):
        self.find_element_and_click("next_btn", "community_page_element")

    def click_next_step(self):
        self.find_element_and_click("next_step_btn", "community_page_element")

    def click_and_input_post_content(self):
        self.find_element_and_sendKeys("input_word", "community_page_element", context="嘿嘿你猜我是谁")

    def click_publish_btn(self):
        self.find_element_and_click("publish_btn", "community_page_element")

    def find_publish_success_toast(self):
        return self.find_toast_by_desc(content="发布成功")

    def to_search_user_by_id(self):
        self.find_element_and_click("search_box", "community_page_element")

    def click_search_box(self):
        self.find_element_and_click("search_input", "community_page_element")

    def input_and_send_search_content(self):
        self.find_element_and_sendKeys("search_input", "community_page_element", context="1092412362", isClick=False)

    def input_enter_search_btn(self):
        self.input_enter_search()

    def click_search_history(self):
        self.find_element_and_click("search_history","community_page_element")

    def click_user_tab(self):
        self.find_element_and_click("user_tab", "community_page_element")

    def click_to_user_page(self):
        self.find_element_and_click("user_name", "community_page_element")

    def click_to_post_content(self):
        self.find_element_and_click("post_item", "community_page_element")

    def click_like_btn(self):
        self.find_element_and_click("like_btn", "community_page_element")

    def get_like_btn_value(self):
        return self.find_element_and_value("like_btn", "community_page_element")

    def click_to_comment_page(self):
        self.find_element_and_click("comment_box", "community_page_element")

    def get_comment_value(self):
        return self.find_element_and_value("comment_btn", "community_page_element")

    def edit_comment(self):
        self.find_element_and_sendKeys("input_comment", "community_page_element", context="下一次", isClick=False)

    def press_comment_btn(self):
        self.find_element_and_click("press_comment","community_page_element")

    def click_share_btn(self):
        self.find_element_and_click("share_btn", "community_page_element")

    def click_delete_btn(self):
        self.find_element_and_click("delete_icon", "community_page_element")

    def click_confirm_delete_btn(self):
        self.find_element_and_click("confirm_delete_post", "community_page_element")

    def get_publisher_name(self):
        return self.find_element_and_value("publisher","community_page_element")
