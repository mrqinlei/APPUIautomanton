# -*- coding: utf-8 -*-

from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest
from utils.string_edit import del_symbol

@allure.feature("测试今日步数模块")
class TestTodayStepsCase:

    @classmethod
    def setup_class(cls):
        cls.todaySteps = BaseDriver.andriod_driver().to_today_steps_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是今日步数类")
        # self.todaySteps.get_device_state_custom()
        statistics_icon = self.todaySteps.get_statistics_icon()
        if statistics_icon is None:
            self.todaySteps = BaseDriver.andriod_driver().to_today_steps_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("今日步数-分享页面测试")
    @allure.severity('Normal')
    @pytest.mark.sportNormal
    @pytest.mark.smoke
    # @allure.issue('http://www.baidu.com',"问题")
    # @allure.testcase('http://www.sina.com', '测试用例')
    def test_share(self):
        """
        测试今日步数页面，点击分享按钮，跳转到分享页面，对两侧数值的一致性进行验证
        :return: 两侧数据一致，PASS
        """
        steps_before = self.todaySteps.get_steps_today_page()
        self.todaySteps.click_share_btn()
        steps_after = self.todaySteps.get_share_steps()
        self.todaySteps.save_screenshots("今日步数页面分享截图")
        self.logInfo.logEnd("今日步数页面分享日志")
        self.todaySteps.click_back_by_native(type="title")
        assert steps_before == steps_after

    @allure.story("今日步数-今日统计页面测试")
    @pytest.mark.smoke
    def test_count_today_day_steps(self):
        """
        测试今日步数统计页面每日点击切换结果
        :return: 点击后页面可查找到符合结果特殊字符即为通过
        """

        self.todaySteps.click_statistics_btn()
        day_count = self.todaySteps.get_step_statistics()
        self.todaySteps.save_screenshots("今日步数统计日页面截图")
        self.logInfo.logEnd("今日步数根据日统计")
        self.todaySteps.click_back_by_native(type="left_btn")
        if "-" not in day_count and "日" in day_count:
            assert "日", "月" in day_count

    @pytest.mark.smoke
    @allure.story("今日步数-统计分享页面测试")
    @allure.severity('Normal')
    @pytest.mark.sportNormal
    def test_share_day_count(self):
        """
        测试今日步数日统计活动时长，活动历程，消耗千卡
        :return: 分享前与分享后数值相等即为通过
        """
        self.todaySteps.click_statistics_btn()
        self.todaySteps.click_statistics_day()
        day_active_steps = self.todaySteps.get_day_active_steps()
        day_active_steps = del_symbol(day_active_steps)
        day_active_time = self.todaySteps.get_day_active_time()
        day_active_miles = self.todaySteps.get_day_active_miles()
        day_active_carolie = self.todaySteps.get_day_use_calorie()
        time.sleep(2)
        self.todaySteps.click_share_btn()
        share_active_steps = self.todaySteps.get_day_share_steps()
        share_active_times = self.todaySteps.get_day_share_times()
        share_active_miles = self.todaySteps.get_day_share_miles()
        share_active_carolie = self.todaySteps.get_day_share_carolie()
        time.sleep(2)
        self.todaySteps.save_screenshots("今日步数统计日页面分享截图")
        self.logInfo.logEnd("今日步数根据日统计分享")
        self.todaySteps.day_share_back_btn()
        self.todaySteps.click_back_by_native(type="left_btn")
        self.todaySteps.click_back_by_native(type="left_btn")
        assert day_active_steps in share_active_steps and \
               share_active_miles == day_active_miles and day_active_carolie == share_active_carolie
                # and day_active_time == share_active_times

    @allure.story("今日步数-周统计页面测试")
    @pytest.mark.smoke
    def test_count_today_week_steps(self):
        """
        测试今日步数统计页面每周点击切换结果
        :return: 点击后页面可查找到符合结果特殊字符即为通过
        """
        self.todaySteps.click_statistics_btn()
        self.todaySteps.click_week_statistics()
        day_count = self.todaySteps.get_step_statistics()
        self.todaySteps.save_screenshots("今日步数统计周页面截图")
        self.logInfo.logEnd("今日步数根据周统计日志")
        self.todaySteps.click_back_by_native(type="left_btn")
        if "-" in day_count:
            assert "日", "月" in day_count

    @allure.story("今日步数-周统计页面分享测试")
    @pytest.mark.smoke
    def test_share_week_count(self):
        """
        测试今日步数周活动时长，活动历程，消耗千卡
        :return: 分享前与分享后数值相等即为通过
        """
        self.todaySteps.click_statistics_btn()
        self.todaySteps.click_week_statistics()
        week_active_miles = self.todaySteps.get_week_active_miles()
        week_active_carolie = self.todaySteps.get_week_active_carolie()
        time.sleep(2)
        self.todaySteps.click_share_btn()
        share_week_miles = self.todaySteps.get_week_share_miles()
        share_week_carolie = self.todaySteps.get_week_share_carolie()
        self.todaySteps.save_screenshots("今日步数统计周页面分享截图")
        self.logInfo.logEnd("今日步数根据周统计分享日志")
        self.todaySteps.click_week_back_btn()
        self.todaySteps.click_back_by_native(type="left_btn")
        assert share_week_miles == week_active_miles and share_week_carolie == week_active_carolie

    @allure.story("今日步数-月统计页面测试")
    @pytest.mark.smoke
    def test_count_today_month_steps(self):
        """
        测试今日步数统计页面每月点击切换结果
        :return: 点击后页面可查找到符合结果特殊字符即为通过
        """
        self.todaySteps.click_statistics_btn()
        self.todaySteps.click_month_statistics()
        day_count = self.todaySteps.get_step_statistics()
        self.todaySteps.save_screenshots("今日步数统计月页面截图")
        self.logInfo.logEnd("今日步数根据月统计")
        self.todaySteps.click_back_by_native(type="left_btn")
        if "年" in day_count:
            assert "年", "月" in day_count

    @allure.story("今日步数-月统计分享页面测试")
    @pytest.mark.smoke
    def test_share_month_count(self):
        """
        测试今日步数月活动时长，活动历程，消耗千卡
        :return: 分享前与分享后数值相等即为通过
        """
        self.todaySteps.click_statistics_btn()
        self.todaySteps.click_month_statistics()
        month_active_miles = self.todaySteps.get_month_active_miles()
        month_active_carolie = self.todaySteps.get_month_active_carolie()
        time.sleep(2)
        self.todaySteps.click_share_btn()
        share_month_miles = self.todaySteps.get_month_share_miles()
        share_month_carolie = self.todaySteps.get_month_share_carolie()
        self.todaySteps.day_share_back_btn()
        self.todaySteps.click_back_by_native(type="left_btn")
        assert month_active_carolie == share_month_carolie and month_active_miles == share_month_miles

    # @allure.story("今日步数-统计-日视图页面测试")
    # @allure.severity('Blocker')
    # # @allure.issue('http://www.baidu.com',"问题")
    # # @allure.testcase('http://www.sina.com', '测试用例')
    # def test_share(self):
    #     """
    #     测试今日步数，统计页面，日试图，界面跳转
    #     :return:可以正确进入统计日试图，PASS
    #     """
    #     self.todaySteps.click_statistics_btn()
    #     #暂时无法定位日视图的控件，暂时不写
    #     self.todaySteps.save_screenshots("今日步数页面分享截图")
    #     self.logInfo.logEnd("今日步数页面分享日志")
    #     assert steps_before == steps_after

    @classmethod
    def teardown_class(cls):
        cls.todaySteps.click_back_by_native(type='left')
        cls.todaySteps.driver.quit()
