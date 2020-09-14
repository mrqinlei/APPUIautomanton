# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


class TestWeight():
    """
    体重模块测试
    """

    def setup_class(cls):
        cls.weight_kg = BaseDriver.andriod_driver().to_weight_page()

    def setup(self):
        # sport_icon = self..get_sport_icon()
        # if sport_icon is None:
        #     self.sport_page.driver.quit()
        #     time.sleep(3)
        #     self.sport_page = BaseDriver.andriod_driver().to_heart_rate_page()
        # else:
        #     pass
        self.logInfo = LogInfo()
    @pytest.mark.skip      #首页布局原因跳过
    def test_weigth_kg(self):
        """
        测试首页心率与点击进入后心率
        :return: 进入后与进入前心率一致则为通过
        """
        get_before_page_weight_kg = self.weight_kg.get_weight_info()
        self.weight_kg.click_weight()
        get_after_weight_kg = self.weight_kg.get_weight_data()
        assert get_after_weight_kg in get_before_page_weight_kg

    @classmethod
    def teardown_class(cls):
        cls.weight_kg.click_back_by_native(type='left_btn')
        cls.weight_kg.driver.quit()
