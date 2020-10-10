# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


@allure.feature("我的设备测试内容")
class TestMyEquipmentCase:

    @classmethod
    def setup_class(cls):
        cls.device = BaseDriver.andriod_driver().to_mine_equipment_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        # message_icon = self.message.get_message_icon()
        # if message_icon is None:
        #     self.message = BaseDriver.andriod_driver().to_mine_page()
        # else:
        #     pass
        self.logInfo = LogInfo()

    @pytest.mark.skip
    # @pytest.mark.smoke
    def test_my_bus_card(self):
        """
        测试我的设备公交卡页面
        :return: 点击可跳转，跳转后页面标题为公交卡即为通过
        """
        self.device.click_my_bus_card()
        bus_card_detail = self.device.get_bus_card_detail()
        assert bus_card_detail == "京津冀互联互通卡 | 免服务费"
        '''
        需要账号已绑定公交卡
        '''

    @classmethod
    def teardown_class(cls):
        cls.device.driver.quit()
