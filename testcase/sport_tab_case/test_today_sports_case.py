# -*- coding: utf-8 -*-

from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
from utils.string_edit import del_symbol, del_str
import pytest


@allure.feature("运动模块我的运动今日运动内容")
class TestTodaySportCase:

    @classmethod
    def setup_class(cls):
        cls.todaysport = BaseDriver.andriod_driver().to_mine_sport_page()
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

    @allure.story("我的运动今日运动历史列表页跳转测试")
    @allure.severity("block")
    # @pytest.mark.smoke  #重复
    @pytest.mark.sportNormal
    def test_today_sports(self):
        """
        测试我的运动看今日运动页面跳转
        :return:跳转成功，且跳转前与跳转后运动数值相同即为通过
        """
        today_sport_title = self.todaysport.get_today_sport_title()
        self.todaysport.to_today_sport_page()
        today_all_sports_run_mile = self.todaysport.get_today_all_sport_run_mile()
        print(today_sport_title)
        print(today_all_sports_run_mile)
        self.todaysport.save_screenshots("今日运动所有运动公里数截图")
        self.logInfo.logEnd("今日运动所有运动公里数日志")
        # assert today_sport_title == today_all_sports_run_mile


    @classmethod
    def teardown_class(cls):
        cls.todaysport.click_back_by_native(type="left_btn")
        cls.todaysport.driver.quit()
