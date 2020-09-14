from base.base_driver import BaseDriver
import time
import pytest
import allure
from utils.log_info import LogInfo
import yaml
from base.base_test_case import BaseTestCase
from utils.server import Server


"""
用于初次登录设置体重功能
"""
@allure.feature("初次登录设置体重内容")
# @pytest.mark.usefixtures("get_devices_list")
class TestLoginCase:

    @classmethod
    def setup_class(cls):
        # self.login_page = BaseDriver().andriod_driver(i=get_devices_list).to_login_page()
        # self.logInfo = LogInfo()
        cls.driver = BaseDriver.andriod_driver()
        cls.login_page = cls.driver.to_login_page()
        cls.logInfo = LogInfo()

    def setup(self):
        self.logInfo = LogInfo()

