# -*- coding: utf-8 -*-

from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
from utils.string_edit import del_symbol, del_str
import pytest


@allure.feature("运动模块我的状态昨晚睡眠")
class TestLastSleep:

    @classmethod
    def setup_class(cls):
        cls.last_sleep = BaseDriver.andriod_driver().to_my_status_sleep_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        share_icon = self.last_sleep.get_sleep()
        if share_icon is None:
            self.last_sleep = BaseDriver.andriod_driver().to_my_status_sleep_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("昨晚睡眠-视图切换页面测试")
    @allure.severity('Blocker')
    @pytest.mark.sleepNormal
    #@pytest.mark.smoke
    def test_last_sleep_day_view(self):
        """
        测试昨晚睡眠日视图切换
        :return:查找到睡眠得分即为通过
        """
        self.last_sleep.click_day_btn()
        last_sleep_score = self.last_sleep.get_sleep_score()
        edit_icon = self.last_sleep.get_edit_icon()
        self.last_sleep.save_screenshots("昨晚睡眠页面日视图截图")
        self.logInfo.logEnd("昨晚睡眠页面日视图日志")
        assert last_sleep_score is not None and edit_icon is not None

    #@pytest.mark.smoke
    def test_last_week_day_view(self):
        """
        测试昨晚睡眠周统计视图
        :return: 点击后若页面展示周睡眠统计即为pass
        """
        self.last_sleep.click_week_btn()
        click_week_result = self.last_sleep.get_click_result()
        self.last_sleep.save_screenshots("昨晚睡眠页面周视图截图")
        self.logInfo.logEnd("昨晚睡眠页面周视图日志")
        assert click_week_result == "周睡眠统计"

    #@pytest.mark.smoke
    def test_last_month_day_view(self):
        """
        测试昨晚睡眠月统计视图
        :return: 点击后若页面展示月睡眠统计即为pass
        """
        self.last_sleep.click_month_btn()
        click_month_result = self.last_sleep.get_click_result()
        self.last_sleep.save_screenshots("昨晚睡眠页面月视图截图")
        self.logInfo.logEnd("昨晚睡眠页面月视图日志")
        assert click_month_result == "月睡眠统计"

    #@pytest.mark.smoke
    def test_last_year_day_view(self):
        """
        测试昨晚睡眠年统计视图
        :return: 点击后若页面展示年睡眠统计即为pass
        """
        self.last_sleep.click_year_btn()
        click_tear_result = self.last_sleep.get_click_result()
        self.last_sleep.save_screenshots("昨晚睡眠页面年视图截图")
        self.logInfo.logEnd("昨晚睡眠页面年视图日志")
        assert click_tear_result == "年睡眠统计"

    @classmethod
    def teardown_class(cls):
        cls.last_sleep.click_back_by_native(type='left')
        cls.last_sleep.driver.quit()
