from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


class TestSleepCase:

    @classmethod
    def setup_class(cls):
        cls.sleep = BaseDriver.andriod_driver().to_sleep_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是睡眠类")
        # self.sleep.get_device_state_custom()
        edit_icon = self.sleep.get_edit_icon()
        if edit_icon is None:
            self.sleep = BaseDriver.andriod_driver().to_sleep_page()
        else:
            pass
        self.logInfo = LogInfo()



    @allure.story("昨晚睡眠-分享页面测试")
    @allure.severity('Blocker')
    # @allure.issue('http://www.baidu.com',"问题")
    # @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.sleepNormal
    def test_share(self):
        """
        测试昨晚睡眠页面，点击分享按钮，跳转到分享页面，对两侧数值的一致性进行验证
        :return: 两侧数据一致，PASS
        """
        time.sleep(3)
        sleep_before = self.sleep.get_sleep_info_value()
        self.sleep.click_share_btn()
        sleep_after = self.sleep.get_sleep_share_value()
        self.sleep.save_screenshots("昨晚睡眠页面分享截图")
        self.logInfo.logEnd("昨晚睡眠页面分享日志")
        self.sleep.click_back_by_native("title")
        # self.sleep.click_back_by_native("left_btn")
        assert sleep_before == sleep_after

    @allure.story("昨晚睡眠-睡眠编辑功能测试")
    @allure.severity('Blocker')
    # @allure.issue('http://www.baidu.com',"问题")
    # @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.sleepP0
    def test_edit_sleep(self):
        """
        测试昨晚睡眠-睡眠编辑功能
        :return:可以成功编辑睡眠记录，PASS
        """
        start_before = self.sleep.get_start_time()
        stop_before = self.sleep.get_stop_time()
        time.sleep(3)
        self.sleep.click_edit_btn()
        self.sleep.click_start_edit()
        time.sleep(1)
        self.sleep.swipe_on('up_bottom_right_to_middle')
        time.sleep(4)
        self.sleep.click_stop_edit()
        self.sleep.swipe_on('up_bottom_right_to_middle')
        time.sleep(4)
        # start_edit = self.sleep.get_start_edit()
        # start_middle = start_edit.split(" ")[2]
        # stop_edit = self.sleep.get_stop_edit()
        # stop_middle = stop_edit.split(" ")[2]
        self.sleep.click_save_btn()
        start_after = self.sleep.get_start_time()
        stop_after = self.sleep.get_stop_time()
        self.sleep.save_screenshots("睡眠编辑截图")
        self.logInfo.logEnd("睡眠编辑日志")
        self.sleep.click_back_by_native("left_btn")
        assert start_before != start_after and stop_before != stop_after



    @classmethod
    def teardown_class(cls):
        # cls.sleep.click_back_by_native(type='left')
        cls.sleep.driver.quit()