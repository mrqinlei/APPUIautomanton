# -*- coding: utf-8 -*-

from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
from utils.string_edit import del_symbol, del_str
import pytest

@allure.feature("运动模块我的运动今日能量测试内容")
class TestTodayEnergyCase:

    @classmethod
    def setup_class(cls):
        cls.today_energy = BaseDriver.andriod_driver().to_weight_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是运动类")
        # self.sport_page.get_device_state_custom()
        # sport_icon = self.todaySport.get_sport_icon()
        # if sport_icon is None:
        #     self.todaySport.driver.quit()
        #     time.sleep(3)
        #     self.todaySport = BaseDriver.andriod_driver().to_mine_sport_page()
        # else:
        #     pass
        self.logInfo = LogInfo()

    @allure.story("我的运动今日能量跳转测试")
    @allure.severity("block")
    @pytest.mark.smoke
    @pytest.mark.sportNormal
    def test_today_energy(self):
        """
        测试我的运动今日能量跳转
        :return: 跳转前后数据一致即为通过
        """
        get_today_energy = self.today_energy.get_energy_main()
        self.today_energy.to_energy_page()
        get_active_energy = self.today_energy.get_energy_page_value()
        self.today_energy.save_screenshots("今日运动今日能量截图")
        self.logInfo.logEnd("今日运动今日能量日志")
        assert get_active_energy == get_today_energy


    @allure.story("我的能量周统计测试")
    @pytest.mark.smoke
    def test_week_energy(self):
        """
        测试每周平均消耗活动能量
        :return: 获取特殊字符"-"成功，即为通过
        """
        self.today_energy.to_energy_page()
        time.sleep(1)
        self.today_energy.click_week_energy_btn()
        get_week_energy = self.today_energy.get_week_and_month_energy_time()
        self.today_energy.save_screenshots("今日运动每周平均消耗能量截图")
        self.logInfo.logEnd("今日运动每周平均消耗能量能量日志")
        assert "-" in get_week_energy

    @allure.story("我的能量月统计测试")
    @pytest.mark.smoke
    def test_month_energy(self):
        """
        测试每月平均消耗活动能量
        :return:
        """
        self.today_energy.to_energy_page()
        time.sleep(1)
        self.today_energy.click_month_energy_btn()
        get_month_energy = self.today_energy.get_week_and_month_energy_time()
        self.today_energy.save_screenshots("今日运动每月平均消耗能量截图")
        self.logInfo.logEnd("今日运动每月平均消耗能量能量日志")
        assert "日" not in get_month_energy

    @classmethod
    def teardown_class(cls):
        cls.today_energy.click_back_by_native(type="left_btn")
        cls.today_energy.driver.quit()
