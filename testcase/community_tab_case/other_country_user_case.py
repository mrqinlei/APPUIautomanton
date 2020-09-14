# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


@allure.feature("社区模块-非大陆用户或非系统语言为非简体中文")
class TestOtherCountryUser:
    """
    测试非大陆用户或非简体中文用户登录后tab展示
    """

    @classmethod
    def setup_class(cls):
        cls.foreign = BaseDriver.andriod_driver().to_other_country_workout_tab()

    def setup(self):
        # foreign_icon = self.foreign.get_foreign_workout_icon()
        # if foreign_icon is None:
        #     self.foreign = BaseDriver.andriod_driver().to_other_country_workout_tab()
        # else:
        #     pass
        self.logInfo = LogInfo()

    @pytest.mark.skip   #需要测试时开启
    @allure.story("非大陆账号登录后tab数量和名称测试")
    @allure.severity('Normal')
    # @pytest.mark.smoke
    @pytest.mark.parametrize("username, password", [
        ("nvs08025@eanok.com", "huami001")
        # ("13522028106", "529614wwy"),
        # ("13269115357", "Zx13269115357")
    ])
    def test_not_chinese_account(self, username, password):
        """
        测试非大陆账号登录后展示tab数量和tab名称
        :return:无社区tab和发现tab且有friends tab 即为通过
        """
        judge_not_chinese_account_login = self.foreign.judge_not_chinese_account_if_login()
        if judge_not_chinese_account_login is not None:
            self.foreign.click_to_not_chinese_mine_page()
            self.foreign.swipe_to_settings_element()
            self.foreign.click_settings_btn()
            self.foreign.click_logout_btn()
            self.foreign.click_confirm_exit_account()
            self.foreign.click_confirm_exit()
            self.foreign.login_by_phone(username, password)
            judge_xiaomi_account = self.foreign.get_judge_xiaomi_account()
            if judge_xiaomi_account is not None:
                self.foreign.click_not_xiaomi_account_login
            else:
                pass
        else:
            self.foreign.login_by_phone(username, password)
            judge_xiaomi_account = self.foreign.get_judge_xiaomi_account()
            if judge_xiaomi_account is not None:
                self.foreign.click_not_xiaomi_account_login
            else:
                pass
        judge_if_have_band = self.foreign.judge_if_have_not_band()
        if judge_if_have_band is not None:
            self.foreign.click_not_have_band_got_it()
        else:
            pass
        isSuccess = self.foreign.get_not_chinese_account_sports_icon()
        self.foreign.save_screenshots("登录截图")
        self.logInfo.logEnd("登录日志")
        not_chinese_account_sports = self.foreign.get_not_chinese_account_sports_icon()
        not_chinese_account_friends = self.foreign.get_not_chinese_account_friends_icon()
        not_chinese_account_mine = self.foreign.get_not_chinese_account_mine_icon()
        self.foreign.click_to_not_chinese_mine_page()
        self.foreign.swipe_to_settings_element()
        self.foreign.click_settings_btn()
        self.foreign.click_logout_btn()
        self.foreign.click_confirm_exit_account()
        self.foreign.click_confirm_exit()
        time.sleep(5)

        assert not_chinese_account_sports is not None and \
               not_chinese_account_friends is not None and not_chinese_account_mine is not None \
               and isSuccess is not None

    @pytest.mark.parametrize("username, password", [
        ("13146085375", "huami001")
        # ("13522028106", "529614wwy"),
        # ("13269115357", "Zx13269115357")
    ])
    @allure.story("大陆账号登录后tab数量和名称测试")
    @allure.severity('Normal')
    @pytest.mark.smoke
    @pytest.mark.skip   #需要测试时开启
    def test_chinese_account(self, username, password):
        """
        测试大陆账号登录后展示tab数量和tab名称
        :return:有社区tab和发现tab即为通过
        """
        judge_login = self.foreign.judge_chinese_account_if_login()
        if judge_login is not None:
            self.foreign.click_to_mine_tab()
            self.foreign.swipe_to_settings_element()
            self.foreign.click_settings_btn()
            self.foreign.click_logout_btn()
            self.foreign.click_confirm_exit_account()
            self.foreign.click_confirm_exit()
            self.foreign.login_by_phone(username, password)
            judge_xiaomi_account = self.foreign.get_judge_xiaomi_account()
            if judge_xiaomi_account is not None:
                self.foreign.click_not_xiaomi_account_login
            else:
                pass
        else:
            self.foreign.login_by_phone(username, password)
            judge_xiaomi_account = self.foreign.get_judge_xiaomi_account()
            if judge_xiaomi_account is not None:
                self.foreign.click_not_xiaomi_account_login
            else:
                pass
        time.sleep(5)
        get_chinese_account_login_sports_tab = self.foreign.get_discover_tab()
        not_chinese_account_friends = self.foreign.get_not_chinese_account_friends_icon()
        assert get_chinese_account_login_sports_tab is not None and \
               not_chinese_account_friends is None

    def teardown(self):
        self.foreign.driver.quit()
