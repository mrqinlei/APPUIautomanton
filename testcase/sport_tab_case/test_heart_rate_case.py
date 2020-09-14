#-*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

class TestHeartRate():

    """
    心率模块测试
    """

    def setup_class(cls):
        cls.heart_rate = BaseDriver.andriod_driver().to_heart_rate_page()

    def setup(self):

        # sport_icon = self..get_sport_icon()
        # if sport_icon is None:
        #     self.sport_page.driver.quit()
        #     time.sleep(3)
        #     self.sport_page = BaseDriver.andriod_driver().to_heart_rate_page()
        # else:
        #     pass
        self.logInfo = LogInfo()

    @pytest.mark.skip   #需要测试时开启
    def test_heart_rate(self):
        """
        测试首页心率与点击进入后心率
        :return: 进入后与进入前心率一致则为通过
        """
        get_before_page_heart_rate = self.heart_rate.get_heart_rate_info()
        self.heart_rate.click_heart_rate()
        get_after_heart_rate = self.heart_rate.get_hr_data()
        print(get_after_heart_rate)
        assert get_after_heart_rate in get_before_page_heart_rate
        ''''
        此处入口为运动首页，有相对布局问题 待解决
        '''

    @classmethod
    def teardown_class(cls):
        cls.heart_rate.click_back_by_native(type='back')
        cls.heart_rate.driver.quit()