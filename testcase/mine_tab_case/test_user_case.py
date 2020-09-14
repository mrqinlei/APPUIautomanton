#-*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

@allure.feature("我的模块测试内容")
class TestUserCase:

    @classmethod
    def setup_class(cls):
        cls.user_page = BaseDriver.andriod_driver().to_mine_page_user()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是用户类")
        # self.user_page.get_device_state_custom()
        add_device_icon = self.user_page.get_add_device_icon()
        if add_device_icon is None:
            self.user_page = BaseDriver.andriod_driver().to_mine_page_user()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("健康周报功能测试")
    @allure.severity('Trivial')
    @allure.issue('http://www.baidu.com', '问题6')
    @allure.testcase('http://www.sina.com', '测试用例6')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_mine_report(self):
        """
        查看健康周报
        :return: 是否成功查看健康周报页面
        """
        self.user_page.to_mine_report()
        title = self.user_page.get_title()
        self.user_page.save_screenshots("查看健康周报截图")
        self.logInfo.logEnd("查看健康周报日志")
        self.user_page.click_back_by_native(type='left')
        assert title == "健康周报"

    @allure.story("设置步数功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题7')
    @allure.testcase("http://www.sina.com", '测试用例7')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_set_steps_goal(self):
        """
        设置步数
        :return: 是否成功设置步数
        """
        self.user_page.swipe_on('up')
        steps_before = self.user_page.get_steps_goal()
        self.user_page.set_goal()
        self.user_page.set_steps_goal()
        time.sleep(2)
        # blue_tooth_tip = self.user_page.get_blue_tooth_tip()
        steps_tip = self.user_page.get_steps_tip()
        while steps_tip is None:
            time.sleep(3)
            # blue_tooth_tip = self.user_page.get_blue_tooth_tip()
            steps_tip = self.user_page.get_steps_tip()
        time.sleep(5)
        self.user_page.swipe_on('up_middle')
        self.user_page.set_steps_goal_confirm()
        steps_after = self.user_page.get_steps_goal()
        self.user_page.save_screenshots("修改步数截图")
        self.logInfo.logEnd("修改步数日志")
        assert steps_before != steps_after


    @allure.story("查看订单功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题9')
    @allure.testcase("http://www.sina.com", '测试用例9')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_order_page(self):
        """
        查看订单功能
        :return: 查看订单功能是否正常
        """
        self.user_page.swipe_on('up')
        self.user_page.to_order_page()
        title = self.user_page.get_title()
        self.user_page.save_screenshots("查看订单截图")
        self.logInfo.logEnd("查看订单日志")
        self.user_page.click_back_by_native(type='left')
        assert title == "我的订单"

    @allure.story("查看行为标注功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题10')
    @allure.testcase("http://www.sina.com", '测试用例10')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_behavior_page(self):
        """
        查看行为标注功能
        :return: 查看行为标注是否正常
        """
        self.user_page.swipe_on('up')
        self.user_page.to_behavior_page()
        title = self.user_page.get_title()
        self.user_page.save_screenshots("查看行为标注截图")
        self.logInfo.logEnd("查看行为标注日志")
        self.user_page.click_back_by_native(type='left')
        assert title == "行为标注"

    @allure.story("查看第三方接入功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题11')
    @allure.testcase("http://www.sina.com", '测试用例11')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_third_page(self):
        """
        查看第三方接入功能
        :return: 查看第三方接入功能是否正常
        """
        self.user_page.swipe_on('up')
        self.user_page.to_third()
        title = self.user_page.get_title()
        self.user_page.save_screenshots("查看第三方接入截图")
        self.logInfo.logEnd("查看第三方接入日志")
        self.user_page.click_back_by_native(type='left')
        assert title == "第三方接入"

    @allure.story("提交意见反馈功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题12')
    @allure.testcase("http://www.sina.com", '测试用例12')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_feed_back(self):
        """
        提交意见反馈功能
        :return: 提交意见反馈功能是否正常
        """
        self.user_page.swipe_on('up')
        self.user_page.to_feed_back_page()
        self.user_page.feed_back_send_keys("测试")
        self.user_page.save_screenshots("提交意见反馈截图")
        self.user_page.to_submit()
        toast = self.user_page.get_toast("提交成功")
        # print("文案为：" + toast)
        self.logInfo.logEnd("提交意见反馈日志")
        assert toast is not None

    #现版本里没有此选项，4.0.19版本里恢复此功能
    @allure.story("查看账号与安全功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题13')
    @allure.testcase("http://www.sina.com", '测试用例13')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_setting_account(self):
        """
        查看账号与安全
        :return: 查看账号与安全是否正常
        """
        self.user_page.swipe_on('up')
        self.user_page.to_setting_page()
        self.user_page.to_account_page()
        time.sleep(1)
        title = self.user_page.get_title()
        self.user_page.save_screenshots("查看账号与安全截图")
        self.logInfo.logEnd("查看账号与安全日志")
        self.user_page.click_back_by_native(type='left')
        self.user_page.click_back_by_native(type='left')
        assert title == "账号与安全"

    @allure.story("查看单位功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题14')
    @allure.testcase("http://www.sina.com", '测试用例14')
    #@pytest.mark.smoke  #查找不到unit元素
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_unit(self):
        """
        查看单位
        :return:查看单位是否正常
        """
        # self.user_page.swipe_on('up')
        self.user_page.to_setting_page()
        self.user_page.to_unit_page()
        time.sleep(2)
        title = self.user_page.get_title()
        self.user_page.save_screenshots("查看单位截图")
        self.logInfo.logEnd("查看单位日志")
        self.user_page.click_back_by_native(type='left')
        self.user_page.click_back_by_native(type='left')
        assert title == "单位"

    @allure.story("改变在通知栏显示连接状态功能测试")
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com", '问题15')
    @allure.testcase("http://www.sina.com", '测试用例15')
    # @pytest.mark.smoke   #无法执行
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_notification_connect_switch(self):
        """
        改变在通知栏显示连接状态
        :return: 改变在通知栏显示连接状态是否成功
        """
        # self.user_page.swipe_on('up')
        self.user_page.to_setting_page()
        time.sleep(3)
        status = self.user_page.get_switch_status()
        time.sleep(1)
        self.user_page.change_switch()
        time.sleep(1)
        self.user_page.save_screenshots("改变在通知栏显示连接状态截图")
        self.logInfo.logEnd("改变在通知栏显示连接状态日志")
        if status == 'true':
            assert self.user_page.get_switch_status() == 'false'
        else:
            assert self.user_page.get_switch_status() == 'true'



    @classmethod
    def teardown_class(cls):
        cls.user_page.driver.quit()

