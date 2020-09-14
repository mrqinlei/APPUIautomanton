#-*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

"""
我的收藏页面的测试内容
"""
@allure.feature("我的收藏模块测试内容")
class TestCollectCase:

    @classmethod
    def setup_class(cls):
        cls.collect = BaseDriver.andriod_driver().to_mine_collect_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        my_collect_icon = self.collect.get_course_tab()
        if my_collect_icon is None:
            self.collect = BaseDriver.andriod_driver().to_mine_collect_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("我的收藏-帖子tab下帖子详情页测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.mineP0
    def test_collect_post_page(self):
        """
        跳转帖子tab下帖子详情页
        :return: 是否成功跳转到帖子详情页面
        """
        time.sleep(3)
        first_name = self.collect.get_first_post_name()
        self.collect.to_first_post_page()
        second_name = self.collect.get_publisher_name()
        self.collect.save_screenshots("查看跳转帖子tab下帖子详情页截图")
        self.logInfo.logEnd("查看帖子tab下帖子详情页日志")
        self.collect.click_back_by_native()
        assert first_name == second_name

    @allure.story("我的收藏-课程tab下课程详情页测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.mineP0
    def test_collect_course_page(self):
        """
        跳转课程tab下课程详情页
        :return: 是否成功跳转到课程详情页面
        """
        time.sleep(5)
        self.collect.to_course_tab()
        first_name = self.collect.get_first_course_name()
        self.collect.to_first_course_page()
        second_name = self.collect.get_course_name()
        self.collect.save_screenshots("查看跳转课程tab下课程详情页截图")
        self.logInfo.logEnd("查看课程tab下课程详情页日志")
        self.collect.click_back_by_native()
        assert first_name == second_name




    @classmethod
    def teardown_class(cls):
        cls.collect.click_back_by_native(type='left')
        cls.collect.driver.quit()
