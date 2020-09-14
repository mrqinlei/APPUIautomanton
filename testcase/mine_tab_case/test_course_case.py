# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
import pytest

from page.mine_tab_page.course_page import CoursePage
from utils.log_info import LogInfo


@allure.feature("我的课程模块测试内容")
class TestCourseCase:

    @classmethod
    def setup_class(cls):
        cls.course = BaseDriver.andriod_driver().to_mine_course_page()
        # cls.course = CoursePage(cls.driver)
        # cls.logInfo = LogInfo()

    def setup(self):
        my_course_icon = self.course.get_add_course_icon()
        if my_course_icon is None:
            self.course = BaseDriver.andriod_driver().to_mine_course_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("我的课程-添加课程测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.mineP0
    def test_add_course(self):
        """
        添加课程
        备注：当课程列表第一个为付费课程时，则无法添加课程
        :return: 是否成功添加课程
        """
        time.sleep(2)
        self.course.to_add_course_list()
        self.course.click_yoga_tab()
        # self.course.find_free_course()
        # time.sleep(10)
        # self.course.click_free_course_label()
        first_course_name = self.course.get_first_course_list_name()
        if first_course_name == "New":
            first_course_name = self.course.get_first_course_list_name_2()
        self.course.to_first_course_list()
        course_name = self.course.get_course_name()
        if first_course_name == course_name:
            self.course.add_coursec_btn()
            self.course.click_back_by_native()
            self.course.click_back_by_native(type='left')
        mine_course_first_name = self.course.get_first_course_name()
        self.course.save_screenshots("查看跳转课程详情页截图")
        self.logInfo.logEnd("查看课程详情页日志")
        # self.course.click_back_by_native(type='left')
        assert mine_course_first_name == first_course_name

    @allure.story("我的课程-课程详情页测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.mineP0
    def test_course_page(self):
        """
        跳转课程详情页
        :return: 是否成功跳转到课程详情页面
        """
        time.sleep(2)
        # self.course.click_to_my_course()
        # self.course.to_add_course_list()
        first_name = self.course.get_first_course_name()
        self.course.to_first_course_page()
        second_name = self.course.get_course_name()
        self.course.save_screenshots("查看跳转课程详情页截图")
        self.logInfo.logEnd("查看课程详情页日志")
        self.course.click_back_by_native()
        assert first_name == second_name

    @allure.story("我的课程-观看课程测试")
    @allure.severity('critical')
    @pytest.mark.smoke
    def test_watch_course(self):
        """
        测试观看课程
        :return:播放视频后查找到播放视频整体surface元素即为通过
        """
        self.course.to_first_course_page()
        time.sleep(3)
        self.course.click_to_course_list()
        self.course.click_to_watch_video()
        video_play_judge = self.course.get_video_play_element()
        self.course.click_to_pause_video()
        self.course.click_to_exit_video()
        self.course.click_feedback()
        self.course.save_screenshots("课程详情视频播放页截图")
        self.logInfo.logEnd("课程详情视频播放页日志")
        self.course.click_back_by_native()
        assert video_play_judge is not None

    @allure.story("我的课程-退出课程测试")
    @allure.severity('critical')
    @pytest.mark.smoke
    def test_exit_course(self):
        """
        测试退出课程
        :return:
        """
        self.course.to_first_course_page()
        time.sleep(1)
        self.course.click_more_btn()
        self.course.click_exit_course_btn()
        after_exit_course = self.course.get_course_info()
        self.course.save_screenshots("退出课程课程详情页截图")
        self.logInfo.logEnd("退出课程日志")
        self.course.click_back_by_native()
        assert after_exit_course is not None and after_exit_course == "学习课程"

    @allure.story("我的课程-添加付费课程测试")
    @allure.severity('critical')
    @pytest.mark.smoke
    def test_add_pay_course(self):
        """
        添加付费课程
        :return: 调起收银台即为通过
        """
        time.sleep(3)
        self.course.to_add_course_list()
        self.course.click_all_tab()
        self.course.find_quality_goods()
        self.course.click_quality_goods_label()
        pay_course_info = self.course.get_buy_course_info()
        self.course.click_to_pay_page()
        time.sleep(1)
        ensure_btn = self.course.get_confirm_pay_btn()
        self.course.save_screenshots("查看购买付费课程页截图")
        self.logInfo.logEnd("查看购买付费课程页日志")
        assert pay_course_info == "购买课程" and ensure_btn == "确认支付"

    @classmethod
    def teardown_class(cls):
        cls.course.click_back_by_native(type='left')
        cls.course.driver.quit()
