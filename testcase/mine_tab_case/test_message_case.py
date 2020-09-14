# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


@allure.feature("亲友模块测试内容")
class TestMessageCase:

    @classmethod
    def setup_class(cls):
        cls.message = BaseDriver.andriod_driver().to_mine_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        message_icon = self.message.get_message_icon()
        if message_icon is None:
            self.message = BaseDriver.andriod_driver().to_mine_page()
        else:
            pass
        self.logInfo = LogInfo()



    @pytest.mark.smoke
    def test_click_to_notification(self):
        """
        测试我的通知，通知页面
        :return: 点击通知后正常跳转即为通过
        """
        self.message.to_message_page()
        self.message.to_notif_tab()
        self.message.to_select_notification_page()
        judge_h5 = self.message.judge_h5_webview()
        if judge_h5 is None:
            notification_name = self.message.get_notification_detail()
            self.message.click_back_by_native(type="back")
            assert notification_name == "详情"
        else:
            assert judge_h5 is not None



    @pytest.mark.smoke
    def test_click_to_message(self):
        """
        测试我的消息，消息页面
        :return:点击消息后可以正常跳转即为通过
        """
        self.message.to_message_page()
        self.message.to_like_and_focus_page()
        self.message.to_like_page()
        self.message.to_like_me_page()
        get_fail_toast = self.message.get_fail_toast()
        if get_fail_toast is None:
            get_post_title = self.message.get_notification_detail()
            self.message.click_back_by_native(type="back")
            self.message.to_follower_page()
            get_follower_element = self.message.find_follower_element()
            self.message.click_back_by_native(type="home_page")
            assert get_post_title == "详情" and get_follower_element is not None
        else:
            self.message.to_follower_page()
            get_follower_element = self.message.find_follower_element()
            self.message.click_back_by_native(type="home_page")
            assert get_follower_element is not None


    @classmethod
    def teardown_class(cls):
        cls.message.driver.quit()
