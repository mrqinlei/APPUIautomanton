#-*- coding: utf-8 -*-

from base.base_page import BasePage

class UserPage(BasePage):


    def get_nick_name(self):
        return self.find_element_and_value("mine_name", "mine_page_element")

    def to_user_info_page(self):
        self.find_element_and_click("mine_person_img", "mine_page_element")

    def get_nick_name_value(self):
        return self.find_elements_and_value("custom_info", "mine_page_element", 0)

    def to_edit_nick_name(self):
        self.find_elements_and_click("custom_key", "mine_page_element", 1)

    def nick_name_send_keys(self, nick_name):
        self.find_element_and_sendKeys("nick_name_edit", "mine_page_element", nick_name)

    def click_save_btn(self):
        self.find_element_and_click("save_btn", "mine_page_element")

    def click_cancel_btn(self):
        self.find_element_and_click("cancel_btn", "mine_page_element")

    def get_my_dynamic_counts(self):
        return self.find_element_and_value("mine_dynamic", "mine_page_element")

    def to_my_zone(self):
        self.find_element_and_click("mine_dynamic", "mine_page_element")

    def get_my_dynamic_num(self):
        return self.find_element_and_value("dynamic_counts", "mine_page_element")

    def get_mine_fans_counts(self):
        return self.find_element_and_value("mine_fans", "mine_page_element")

    def to_mine_fans_page(self):
        self.find_element_and_click("mine_fans", "mine_page_element")

    def get_mine_fans_list(self):
        return self.find_elements("mine_fans_list", "mine_page_element")

    def to_mine_course(self):
        self.find_element_and_click("mine_course", "mine_page_element")

    def to_mine_dedal(self):
        self.find_element_and_click("mine_dedal", "mine_page_element")

    def to_mine_favorite(self):
        self.find_element_and_click("mine_favorite", "mine_page_element")

    def to_mine_report(self):
        self.find_element_and_click("mine_report", "mine_page_element")

    def get_title(self):
        return self.find_element_and_value("title", "mine_page_element")

    def get_steps_goal(self):
        return self.find_element_and_value("step_goal", "mine_page_element")

    def get_weight_goal(self):
        return self.find_element_and_value("weight_goal", "mine_page_element")

    def set_goal(self):
        self.find_element_and_click("step_goal", "mine_page_element")

    def set_steps_goal(self):
        self.find_element_and_click("step_goal_btn", "mine_page_element")

    def set_weight_goal(self):
        self.find_element_and_click("weight_goal_btn", "mine_page_element")

    def set_steps_goal_confirm(self):
        self.find_element_and_click("step_gola_confirm", "mine_page_element")

    def get_blue_tooth_tip(self):
        return self.find_element("bluetooth_tip", "mine_page_element")

    def get_steps_tip(self):
        return self.find_element("step_tips", "mine_page_element")

    def to_friend_page(self):
        self.find_element_and_click("friend_layout", "mine_page_element")

    def get_friend_name(self):
        return self.find_elements_and_value("friend_name", "mine_page_element")

    def to_friend_info_page(self):
        self.find_element_and_click("friend_list", "mine_page_element")

    def to_order_page(self):
        self.find_element_and_click("order_layout", "mine_page_element")

    def to_behavior_page(self):
        self.find_element_and_click("behavior", "mine_page_element")

    def to_third(self):
        self.find_element_and_click("third", "mine_page_element")

    def to_feed_back_page(self):
        self.find_element_and_click("feed_back", "mine_page_element")

    def feed_back_send_keys(self, content):
        self.find_element_and_sendKeys("content", "mine_page_element", content)

    def to_submit(self):
        self.find_element_and_click("right_btn", "mine_page_element")

    def get_toast(self, content):
        return self.find_toast_by_desc(content)

    def to_setting_page(self):
        self.find_element_and_click("setting_layout", "mine_page_element")

    def to_account_page(self):
        self.find_element_and_click("account_bind", "mine_page_element")

    def to_unit_page(self):
        self.find_element_and_click("unit_layout", "mine_page_element")

    def get_switch_status(self):
        return self.find_element_and_name("switch_status", "mine_page_element", "checked")

    def change_switch(self):
        self.find_element_and_click("switch_status", "mine_page_element")

    def to_clear_cache_page(self):
        self.find_element_and_click("clear_cache_layout", "mine_page_element")

    def get_cache_value(self):
        self.find_element_and_value("custom_info", "mine_page_element")

    def clear_cache(self):
        self.find_element_and_click("train_cache", "mine_page_element")

    def dialog_positive_btn(self):
        self.find_element_and_click("weight_goal_btn", "mine_page_element")

    def to_update_page(self):
        self.find_element_and_click("update_layout", "mine_page_element")

    def to_about_page(self):
        self.find_element_and_click("about_layout", "mine_page_element")

    def logout_btn(self):
        self.find_element_and_click("logout_btn", "mine_page_element")

    def get_add_device_icon(self):
        return self.find_element("add_device_btn", "mine_page_element")
