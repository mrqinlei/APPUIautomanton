# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

@allure.feature("运动模块-我的运动页面测试")
class TestMySports:
    """
    运动模块-我的运动测试
    """

    @classmethod
    def setup_class(cls):
        cls.my_sports = BaseDriver.andriod_driver().to_my_sports_page()

    def setup(self):
        my_sports_icon = self.my_sports.get_my_sports_icon()
        if my_sports_icon is None:
            self.my_sports = BaseDriver.andriod_driver().to_my_sports_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("今日运动列表-列表展示页面测试")
    @pytest.mark.smoke
    def test_my_sports_show(self):
        """
        运动模块-我的运动列表展示
        :return:列表内展示：今日步数、今日运动、今日能量、连续达标
        """
        get_today_steps_icon = self.my_sports.get_my_sports_icon()
        get_today_sports_icon = self.my_sports.get_before_today_steps_miles()
        get_today_energy_icon = self.my_sports.get_before_today_energy()
        self.my_sports.swipe_on(direction="up_middle")
        get_today_goal_icon = self.my_sports.get_before_goal()
        assert get_today_steps_icon is not None and get_today_sports_icon is not None \
               and get_today_energy_icon is not None and get_today_goal_icon is not None
        self.my_sports.save_screenshots("查看运动-我的运动-页面截图")
        self.logInfo.logEnd("查看运动-我的运动-页面日志")

    @allure.story("今日运动列表-运动距离和步数跳转页面测试")
    @pytest.mark.smoke
    def test_today_steps_value(self):
        """
        测试-运动模块-我的运动-今日步数-运动距离
        :return: 步数展示-距离展示-今日展示
        """
        self.my_sports.swipe_on(direction="down")
        get_before_today_steps = self.my_sports.get_before_today_steps()
        get_before_today_steps = get_before_today_steps.split(' ')[1]
        get_before_today_steps_distance = self.my_sports.get_before_today_steps_miles()
        get_before_today_steps_distance = get_before_today_steps_distance.split("步数运动距离")[1]
        self.my_sports.click_to_today_steps_page()
        get_after_today_steps = self.my_sports.get_after_today_steps()
        get_after_today_distance = self.my_sports.get_after_today_steps_distance()
        get_after_today_distance = get_after_today_distance.split("距离")[1]
        get_after_today_carol = self.my_sports.get_after_today_steps_carol()
        print(get_after_today_distance,get_before_today_steps_distance)
        self.my_sports.save_screenshots("查看运动-我的运动-今日步数页面截图")
        self.logInfo.logEnd("查看运动-我的运动-今日步数页面日志")
        self.my_sports.click_back_by_native(type="left_btn")
        if get_after_today_carol is not None:
            assert get_before_today_steps in get_after_today_steps

    @allure.story("今日运动列表-我的运动跳转页面测试")
    @pytest.mark.smoke
    def test_today_my_steps(self):
        """
        测试运动模块-我的运动-今日步数进入前与进入后步数数值
        :return: 一致即为通过
        """
        get_before_today_steps = self.my_sports.get_before_today_steps()
        get_before_today_steps = get_before_today_steps.split(' ')[1]
        self.my_sports.click_to_today_steps_page()
        get_after_today_steps = self.my_sports.get_after_today_steps()
        print(get_before_today_steps)
        print(get_after_today_steps)
        self.my_sports.save_screenshots("查看运动-我的运动-今日步数截图")
        self.logInfo.logEnd("查看运动-我的运动-今日步数日志")
        self.my_sports.click_back_by_native(type="left_btn")
        assert get_before_today_steps in get_after_today_steps

    @allure.story("今日运动列表-今日运动跳转页面测试")
    @pytest.mark.smoke
    def test_today_sports(self):
        """
        测试运动模块-我的运动-今日运动进入前与进入后运动公里
        :return:前后数值一致则为通过
        """
        get_before_today_sports_miles = self.my_sports.get_before_today_sports_miles()
        get_before_today_sports_miles = get_before_today_sports_miles.split("分")[1]
        self.my_sports.click_to_today_sports_miles_page()
        self.my_sports.click_count_by_week()
        get_after_today_sports_miles = self.my_sports.get_after_today_sports_miles()
        self.my_sports.save_screenshots("查看运动-我的运动-今日运动截图")
        self.logInfo.logEnd("查看运动-我的运动-今日运动日志")
        self.my_sports.click_back_by_native(type="left_btn")
        assert get_after_today_sports_miles in get_before_today_sports_miles

    @allure.story("今日运动列表-今日能量跳转页面测试")
    @pytest.mark.smoke
    def test_today_energy(self):
        """
        测试运动模块-我的运动-今日能量进入前与进入后能量数值
        :return:前后数值一致则为通过
        """
        get_before_today_energy = self.my_sports.get_before_today_energy()
        self.my_sports.click_to_today_energy_page()
        get_after_today_energy = self.my_sports.get_after_today_energy()
        self.my_sports.save_screenshots("查看运动-我的运动-今日能量截图")
        self.logInfo.logEnd("查看运动-我的运动-今日能量日志")
        self.my_sports.click_back_by_native(type="left_btn")
        assert get_after_today_energy in get_before_today_energy

    @allure.story("今日运动列-今日跳转页面测试")
    @pytest.mark.smoke
    def test_today_goal(self):
        """
        测试运动模块-我的运动-今日达标进入前与进入后能量数值
        :return:前后数值一致则为通过
        """
        self.my_sports.swipe_on(direction="up")
        get_before_goal_value = self.my_sports.get_before_goal()
        get_before_goal_value = get_before_goal_value.split(" ")[1]
        self.my_sports.click_to_goal_page()
        get_after_goal_value = self.my_sports.get_after_goal()
        self.my_sports.save_screenshots("查看运动-我的运动-今日达标截图")
        self.logInfo.logEnd("查看运动-我的运动-今日达标日志")
        self.my_sports.click_goal_back_to_my_sports
        assert get_before_goal_value in get_after_goal_value



    @classmethod
    def teardown_class(cls):
        cls.my_sports.driver.quit()
