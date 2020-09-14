#-*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

@allure.feature("亲友模块测试内容")
class TestFriendsCase:

    @classmethod
    def setup_class(cls):
        cls.friends = BaseDriver.andriod_driver().to_mine_friends_page()
        # cls.logInfo = LogInfo()


    def setup(self):
        my_friends_icon = self.friends.get_first_friend_name()
        if my_friends_icon is None:
            self.friends = BaseDriver.andriod_driver().to_mine_friends_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("亲友-亲友详情页测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.mineP0
    def test_care(self):
        """
        跳转亲友详情页
        :return: 是否成功跳转到亲友详情页面
        """
        first_name = self.friends.get_first_friend_name()
        first_steps = self.friends.get_first_friend_steps()
        first_sleep = self.friends.get_first_friend_sleep()
        first_weight = self.friends.get_first_friend_weight()
        self.friends.click_first_friend_layout()
        person_name = self.friends.get_person_name()
        person_steps = self.friends.get_person_steps()
        person_sleep = self.friends.get_person_sleep()
        person_weight = self.friends.get_person_weight()
        self.friends.save_screenshots("查看跳转亲友详情页截图")
        self.logInfo.logEnd("查看亲友详情页日志")
        assert first_name == person_name and first_steps == person_steps and first_sleep == person_sleep and first_weight == person_weight



    @classmethod
    def teardown_class(cls):
        # cls.friends.click_back_by_native(type="friend")
        cls.friends.driver.quit()
