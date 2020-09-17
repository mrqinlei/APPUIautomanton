#-*- coding: utf-8 -*-

from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

@allure.feature("我的-个人信息页面测试内容")
class TestUserInfoCase:

    @classmethod
    def setup_class(cls):
        cls.user_info = BaseDriver.andriod_driver().to_mine_user_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是用户信息类")
        # self.user_info.get_device_state_custom()
        nick_name_icon = self.user_info.get_nick_name_value()
        if nick_name_icon is None:
            self.user_info = BaseDriver.andriod_driver().to_mine_user_page()
        else:
            pass
        self.logInfo = LogInfo()
    @pytest.mark.todisplay
    @allure.story("修改昵称功能测试")
    @allure.severity('Blocker')
    @allure.issue('http://www.baidu.com', "问题")
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.mineNormal
    @pytest.mark.smoke
    @pytest.mark.parametrize("username", [
        "username1",
        "username2",
        "username3"
    ])
    def test_edit_nick_name(self, username):
        '''
        修改用户昵称
        :return:是否成功修改昵称
        '''
        nick_name_before = self.user_info.get_nick_name_value()
        self.user_info.to_edit_nick_name()
        # self.user_info.nick_name_send_keys(nick_name_before + "1")
        self.user_info.nick_name_send_keys(username)
        self.user_info.click_save_btn()
        nick_name_middle = self.user_info.get_nick_name_value()
        self.user_info.save_screenshots("修改昵称截图")
        self.logInfo.logEnd("修改昵称日志")
        assert nick_name_before != nick_name_middle

    @pytest.mark.todisplay
    @allure.story("修改性别功能测试")
    @allure.severity('Blocker')
    @allure.issue('http://www.baidu.com', "问题")
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.mineNormal
    @pytest.mark.smoke
    def test_edit_sex(self):
        '''
        修改用户性别
        :return:是否成功修改性别
        '''
        sex_value = self.user_info.get_sex_value()
        self.user_info.to_edit_sex()
        if sex_value == '男':
            self.user_info.chose_female_btn()
        else:
            self.user_info.chose_male_btn()
        sex_value_after = self.user_info.get_sex_value()
        self.user_info.save_screenshots("修改性别截图")
        self.logInfo.logEnd("修改性别日志")
        assert sex_value != sex_value_after

    @pytest.mark.todisplay
    @allure.story("修改身高功能测试")
    @allure.severity('Blocker')
    @allure.issue('http://www.baidu.com', "问题")
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.mineNormal
    def test_edit_height(self):
        '''
        修改用户身高
        :return:是否成功修改身高
        '''
        height_value = self.user_info.get_height_value()
        self.user_info.to_edit_height()
        self.user_info.swipe_on('up')
        time.sleep(2)
        self.user_info.save_height()
        height_value_after = self.user_info.get_height_value()
        self.user_info.save_screenshots("修改身高截图")
        self.logInfo.logEnd("修改身高日志")
        assert height_value != height_value_after

    @allure.story("编辑个人简介功能测试")
    @allure.severity('Blocker')
    @allure.issue('http://www.baidu.com', "问题")
    @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.mineNormal
    @pytest.mark.smoke
    def test_edit_brief(self):
        '''
        修改个人简介
        :return:是否成功修改个人简介
        '''
        brief_content = self.user_info.get_brief()
        self.user_info.to_edit_brief_page()
        self.user_info.edit_brief(brief_content + "1")
        self.user_info.save_brief()
        brief_content_after = self.user_info.get_brief()
        self.user_info.save_screenshots("修改个人简介截图")
        self.logInfo.logEnd("修改个人简介日志")
        assert brief_content != brief_content_after

    # @pytest.mark.smoke
    # def test_edit_photo(self):
    #     '''
    #     修改个人头像
    #     :return:是否成功修改后成功返回个人信息页面
    #     '''
    #     before_photo_element = self.user_info.get_image_element()
    #     self.user_info.to_image_page()
    #     self.user_info.click_local_photo()
    #     self.user_info.click_select_photo()
    #     self.user_info.confirm_photo()
    #     after_photo_element = self.user_info.get_image_element()
    #     self.user_info.save_screenshots("修改个人照片截图")
    #     self.logInfo.logEnd("修改个人照片日志")
    #     assert before_photo_element is not None and\
    #             after_photo_element is not None
    '''
    选择相片是系统控件 无法操作
    '''


    @classmethod
    def teardown_class(cls):
        # cls.user_info.click_back_by_native(type='left')
        cls.user_info.driver.quit()
