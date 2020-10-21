from base.base_driver import BaseDriver
import time
import pytest
import allure
from utils.log_info import LogInfo
import yaml
from base.base_test_case import BaseTestCase
from utils.server import Server


"""
此模块用于测试小米运动的登录功能
包括手机号登录、邮箱登录、第三方登录
"""
@allure.feature("登录模块测试内容")
# @pytest.mark.usefixtures("get_devices_list")
class TestLoginCase:

    @classmethod
    def setup_class(cls):
        # self.login_page = BaseDriver().andriod_driver(i=get_devices_list).to_login_page()
        # self.logInfo = LogInfo()
        cls.driver = BaseDriver.andriod_driver()
        cls.login_page = cls.driver.to_login_page()
        cls.logInfo = LogInfo()
        # pass

    @pytest.mark.parametrize("username, password", [
        ("18601331124", "huami001")
        # ("13522028106", "529614wwy"),
        # ("13269115357", "Zx13269115357")
    ])
    @allure.story("手机号登录功能测试")
    @allure.severity('Blocker')
    @allure.issue('http://www.baidu.com',"问题")
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.loginAndRigisterP0
    @pytest.mark.core
    @pytest.mark.release
    # @pytest.mark.usefixtures('get_devices_list')
    def test_login_by_phone(self, username, password):
    # def test_login_by_phone(self, get_devices_list):
        """
        手机号登录功能测试
        :return:登录成功返回True
        """
        # self.login_page = get_devices_list.to_login_page()
        # self.logInfo = LogInfo()
        # self.login_page.login_by_phone("18310951039", "huami001001")
        self.login_page.login_by_phone(username, password)
        isSuccess = self.login_page.get_sport_tab()
        self.login_page.save_screenshots("登录截图")
        self.logInfo.logEnd("登录日志")
        assert isSuccess is not None


    # def test_login(self):
    #     BaseTestCase("/Users/huami/Documents/MitFitAutoTest/case/login.yaml").run(self.driver)

    #需要打开Debug模式WebView.setWebContentsDebuggingEnabled(true);
    # def test_login_by_xm(self):
    #     self.login_page.to_xiaomi_login_page()
    #     time.sleep(5)
    #     self.login_page.switch_to_webview()
    #     time.sleep(3)
    #     switch_btn = self.login_page.get_switch_btn()
    #     if switch_btn is not None:
    #         self.login_page.click_switch_btn()
    #     self.login_page.edit_username_xiaomi("18310951039")
    #     self.login_page.edit_pwd_xiaomi("0928Zwei")
    #     self.login_page.click_login_xiaomi()
    #     isSuccess = self.login_page.get_login_success_toast("登录成功")
    #     assert isSuccess is not None


    def teardown(self):
        # self.driver.quit()
        pass