# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


@allure.feature("运动模块-我的状态测试")
class TestMyStatus():
    """
    运动模块-我的状态测试
    """

    @classmethod
    def setup_class(cls):
        cls.my_status = BaseDriver.andriod_driver().to_my_status_page()

    def setup(self):
        my_status_icon = self.my_status.get_my_status_icon()
        if my_status_icon is None:
            self.my_status = BaseDriver.andriod_driver().to_my_status_page()
        else:
            pass
        self.logInfo = LogInfo()

    @pytest.mark.smoke
    def test_pai_value(self):
        """
        测试pai值我的状态页面展示数值与点击进入后数值
        :return: 一致则通过
        """
        get_before_all_pai_value = self.my_status.get_before_pai_value()
        get_before_today_pai_value = self.my_status.get_today_pai_value()
        self.my_status.click_to_pai_page()
        judge_if_pai_guide_exist = self.my_status.find_pai_guide_element()
        if judge_if_pai_guide_exist is not None:
            self.my_status.swipe_on("up")
        else:
            pass
        get_after_all_pai_value = self.my_status.get_after_all_pai_value()
        get_after_today_pai_value = self.my_status.get_after_today_pai_value()
        get_after_today_pai_value = get_after_today_pai_value.split("P")[0]
        self.my_status.save_screenshots("查看运动-我的状态-PAI值截图")
        self.logInfo.logEnd("查看运动-我的状态-PAI值日志")
        self.my_status.click_back_by_native(type="left_btn")
        time.sleep(1)
        assert get_after_all_pai_value in get_before_all_pai_value and \
               get_after_today_pai_value in get_before_today_pai_value

    @pytest.mark.smoke
    def test_press_value(self):
        """
        测试运动-我的状态-压力值和点击进入后压力值
        :return: 数值一致即为通过
        """
        get_before_press = self.my_status.get_before_recent_press()
        self.my_status.click_to_press_page()
        get_after_press = self.my_status.get_after_recent_press()
        self.my_status.save_screenshots("查看运动-我的状态-压力值截图")
        self.logInfo.logEnd("查看运动-我的状态-压力值日志")
        self.my_status.click_back_by_native(type="left_btn")
        time.sleep(1)
        assert get_after_press in get_before_press

    @pytest.mark.smoke
    def test_heart_rate(self):
        """
        测试运动-我的状态-心率数值和点击进入后数值
        :return: 进入前后心率数值相同即为通过
        """
        get_before_heart_rate = self.my_status.get_before_heart_rate()
        self.my_status.click_to_heart_rate_page()
        time.sleep(1)
        get_after_heart_rate = self.my_status.get_after_heart_rate()
        self.my_status.save_screenshots("查看运动-我的状态-心率截图")
        self.logInfo.logEnd("查看运动-我的状态-心率日志")
        self.my_status.click_back_by_native(type="left_btn")
        assert get_after_heart_rate in get_before_heart_rate


    # @pytest.mark.smoke    #展示用暂时注释，需考虑无数据时场景
    def test_last_sleep(self):
        """
        测试运动-我的状态-睡眠卡片跳转
        :return:跳转前与跳转后睡眠时间相同即为通过
        """
        # get_sleep_element = self.my_status.find_before_last_sleep_element()
        self.my_status.swipe_to_half()
        get_before_sleep_time = self.my_status.get_before_sleep_time()
        get_before_sleep_time = get_before_sleep_time.split("昨晚睡眠 ")[1]
        self.my_status.click_to_sleep_page()
        get_after_sleep_time = self.my_status.get_after_sleep_time()
        self.my_status.save_screenshots("查看运动-我的状态-睡眠截图")
        self.logInfo.logEnd("查看运动-我的状态-睡眠日志")
        self.my_status.click_back_by_native(type="left_btn")
        assert get_before_sleep_time == get_after_sleep_time

    # @pytest.mark.smoke  #演示原因 暂时注释
    def test_a_few_sleep(self):
        """
        测试运动-我的状态-零星小睡跳转
        :return:
        """
        self.my_status.find_before_last_sleep_element()
        self.my_status.click_to_sleep_page()
        get_before_little_sleep = self.my_status.get_before_little_sleep_time()
        self.my_status.click_to_little_sleep()
        get_after_little_sleep = self.my_status.get_after_little_sleep_time()
        print(get_after_little_sleep,get_before_little_sleep)
        self.my_status.click_back_by_native(type="back")
        self.my_status.click_back_by_native(type="back")



    @pytest.mark.smoke
    def test_weight_kilogram(self):
        """
        测试运动-我的状态-体重数值进入前与进入后
        :return: 数值相同即为pass
        """
        # self.my_status.swipe_to_bottle()
        self.my_status.find_before_weight_value()
        get_before_weight = self.my_status.get_before_weight_value()
        self.my_status.click_to_weight_page()
        time.sleep(1)
        get_after_weight = self.my_status.get_after_weight_value()
        self.my_status.save_screenshots("查看运动-我的状态-体重截图")
        self.logInfo.logEnd("查看运动-我的状态-体重日志")
        self.my_status.click_back_by_native(type="left_btn")
        assert get_after_weight in get_before_weight
        '''
        由于体重元素不在屏幕展示范围内，需要先执行滑动，再查找元素 待解决
        '''
    @pytest.mark.smoke
    def test_body_fat(self):
        """
        测试运动-我的状态-身体指数卡片跳转
        :return:跳转前与跳转后身体指数相同即为通过
        """
        # self.my_status.swipe_to_bottle()
        self.my_status.find_body_fat_element()
        before_body_fat = self.my_status.get_before_body_fat()
        before_body_fat = before_body_fat.split(" ")[1]
        self.my_status.click_to_body_fat_page()
        after_body_fat = self.my_status.get_after_body_fat()
        self.my_status.save_screenshots("查看运动-我的状态-身体指数截图")
        self.logInfo.logEnd("查看运动-我的状态-身体指数日志")
        self.my_status.click_back_by_native(type="left_btn")
        assert before_body_fat in after_body_fat

    @pytest.mark.smoke
    def test_balance(self):
        """
        测试运动-我的状态-平衡性卡片跳转
        :return: 点击前后页面平衡性一致即为通过
        """
        # self.my_status.swipe_to_bottle()
        self.my_status.find_balance_element()
        before_balance = self.my_status.get_before_balance()
        before_balance = before_balance.split(" ")[1]
        self.my_status.click_to_balance_page()
        time.sleep(1)
        after_balance = self.my_status.get_after_balance()
        self.my_status.save_screenshots("查看运动-我的状态-平衡性截图")
        self.logInfo.logEnd("查看运动-我的状态-平衡性日志")
        self.my_status.click_back_by_native(type="left_btn")
        assert after_balance in before_balance

    @classmethod
    def teardown_class(cls):
        cls.my_status.driver.quit()
