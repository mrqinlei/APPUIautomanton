#-*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

@allure.feature("个人社区主页模块测试内容")
class TestPersonalHomepageCase:

    @classmethod
    def setup_class(cls):
        cls.homepage = BaseDriver.andriod_driver().to_mine_personal_homepage()
        # cls.logInfo = LogInfo()


    def setup(self):
        # print ("这是个人主页类")
        # self.homepage.get_device_state_custom()
        edit_profile_icon = self.homepage.get_edit_profile_icon()
        if edit_profile_icon is None:
            self.homepage = BaseDriver.andriod_driver().to_mine_personal_homepage()
        else:
            pass
        self.logInfo = LogInfo()




    @allure.story("个人主页-我的关注测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke   #展示用暂时注释
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_care(self):
        """
        查看我的关注页面
        :return: 是否成功查看我的关注页面
        """
        self.homepage.click_care_btn()
        title = self.homepage.get_title()
        self.homepage.save_screenshots("查看个人主页-我的关注页面截图")
        self.logInfo.logEnd("查看个人主页-我的关注页面日志")
        self.homepage.click_back_by_native(type='left')
        assert title == "我的关注"

    @allure.story("个人主页-我的粉丝测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.mineP0
    def test_fans(self):
        """
        查看我的粉丝页面
        :return: 是否成功查看我的粉丝页面
        """
        self.homepage.click_fans_btn()
        title = self.homepage.get_title()
        self.homepage.save_screenshots("查看个人主页-我的粉丝页面截图")
        self.logInfo.logEnd("查看个人主页-我的粉丝页面日志")
        self.homepage.click_back_by_native(type='left')
        assert title == "我的粉丝"

    @allure.story("个人主页-编辑资料按钮跳转功能测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_edit_profile(self):
        """
        查看个人主页-编辑资料按钮跳转功能
        :return: 是否成功跳转到个人信息页面
        """
        self.homepage.click_person_profile()
        title = self.homepage.get_title()
        self.homepage.save_screenshots("查看个人主页-编辑资料按钮跳转功能截图")
        self.logInfo.logEnd("查看个人主页-编辑资料按钮跳转功能日志")
        self.homepage.click_back_by_native(type='left')
        assert title == "个人信息"

    @allure.story("个人主页-更多勋章按钮跳转功能测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_medal_page(self):
        """
        查看个人主页-更多勋章按钮跳转功能
        :return: 是否成功跳转到我的勋章页面
        """
        self.homepage.to_medal_page()
        title = self.homepage.get_title()
        self.homepage.save_screenshots("查看个人主页-更多勋章按钮跳转功能截图")
        self.logInfo.logEnd("查看个人主页-更多勋章按钮跳转功能日志")
        time.sleep(2)
        self.homepage.click_back_by_native(type='left')
        assert title == "我的勋章"

    @allure.story("个人主页-我的日记本跳转功能测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_diary_page(self):
        """
        查看个人主页-我的日记本跳转功能
        :return: 是否成功跳转到我的日记本页面
        """
        time.sleep(3)
        self.homepage.to_diary_page()
        title = self.homepage.get_title()
        self.homepage.save_screenshots("查看个人主页-我的日记本跳转功能截图")
        self.logInfo.logEnd("查看个人主页-我的日记本跳转功能日志")
        self.homepage.click_back_by_native(type='left')
        assert title == "日记本"

    @allure.story("个人主页-动态tab下帖子跳转功能测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_dynamic_page(self):
        """
        查看个人主页-动态tab下帖子跳转功能
        :return: 是否成功跳转到帖子页面
        """
        time.sleep(2)
        first_name = self.homepage.get_first_post_name()
        self.homepage.to_post_page()
        time.sleep(3)
        self.homepage.swipe_on('down')
        nick_name = self.homepage.get_publisher_name()
        self.homepage.save_screenshots("查看个人主页-动态tab下帖子跳转功能截图")
        self.logInfo.logEnd("查看个人主页-动态tab下帖子跳转功能日志")
        self.homepage.click_back_by_native()
        assert first_name == nick_name

    @allure.story("个人主页-视频tab下帖子跳转功能测试")
    @allure.severity('critical')
    @allure.issue('http://www.baidu.com', '问题')
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.smoke
    @pytest.mark.skip    #当前账号无权限
    @pytest.mark.release
    @pytest.mark.core
    @pytest.mark.mineP0
    def test_video_page(self):
        """
        查看个人主页-视频tab下帖子跳转功能
        :return: 是否成功跳转到帖子页面
        """
        self.homepage.click_video_tab()
        time.sleep(2)
        first_name = self.homepage.get_first_post_name()
        self.homepage.to_post_page()
        time.sleep(3)
        self.homepage.swipe_on('down')
        second_name = self.homepage.get_publisher_name()
        self.homepage.save_screenshots("查看个人主页-视频tab下帖子跳转功能截图")
        self.logInfo.logEnd("查看个人主页-视频tab下帖子跳转功能日志")
        self.homepage.click_back_by_native()
        assert first_name == second_name


    @classmethod
    def teardown_class(cls):
        # cls.homepage.click_back_by_native(type="home_page")
        cls.homepage.driver.quit()
