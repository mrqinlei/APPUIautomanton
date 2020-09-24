# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


@allure.feature("社区测试内容")
class TestMyDynamic:
    """
    测试我的tab下我的动态下动态展示和帖子点赞评论删除操作
    """

    @classmethod
    def setup_class(cls):
        cls.dynamic = BaseDriver.andriod_driver().to_my_dynamic_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        edit_profile_icon = self.dynamic.get_edit_profile_icon()
        if edit_profile_icon is None:
            self.dynamic = BaseDriver.andriod_driver().to_my_dynamic_page()
        else:
            pass
        self.logInfo = LogInfo()

    @allure.story("个人主页-动态tab下帖子跳转功能测试")
    @allure.severity('critical')
    @pytest.mark.smoke
    def test_dynamic_page(self):
        """
        查看个人主页-动态tab下帖子跳转功能
        :return: 是否成功跳转到帖子页面
        """
        time.sleep(2)
        first_name = self.dynamic.get_first_post_name()
        self.dynamic.to_post_page()
        time.sleep(3)
        self.dynamic.swipe_on('down')
        nick_name = self.dynamic.get_publisher_name()
        self.dynamic.save_screenshots("查看个人主页-动态tab下帖子跳转功能截图")
        self.logInfo.logEnd("查看个人主页-动态tab下帖子跳转功能日志")
        self.dynamic.click_back_by_native()
        assert first_name == nick_name

    @allure.story("个人主页-动态tab下帖子点赞测试")
    @pytest.mark.smoke
    def test_dynamic_like_post(self):
        """
        测试对社区帖子进行点赞
        :return:若帖子点赞数为0则点赞后数量为1，若>0,则点赞后结果加一，或取消点赞，结果减一
        """
        self.dynamic.to_post_page()
        before_press_like_btn = self.dynamic.get_like_btn_value()
        if before_press_like_btn == "点赞":
            self.dynamic.click_like_btn()
            time.sleep(1)
            after_press_like_btn = self.dynamic.get_like_btn_value()
            self.dynamic.save_screenshots("社区tab帖子点赞功能截图")
            self.logInfo.logEnd("社区tab帖子点赞功能日志")
            assert after_press_like_btn == '1'
        else:
            before_press_like_btn = int(before_press_like_btn)
            self.dynamic.save_screenshots("社区tab帖子点赞功能截图")
            self.logInfo.logEnd("社区tab帖子点赞功能日志")
            self.dynamic.click_like_btn()
            time.sleep(1)
            after_press_like_btn = int(self.dynamic.get_like_btn_value())
            assert after_press_like_btn == before_press_like_btn + 1 \
                   or after_press_like_btn == before_press_like_btn - 1

    @allure.story("个人主页-动态tab下帖子评论功能测试")
    @pytest.mark.smoke
    def test_dynamic_comment_post(self):
        """
        测试对帖子评论功能
        :return:帖子评论数为0时，评论后返回结果为1，或当前评论数>1时，返回结果为评论数+1即为通过
        """
        self.dynamic.to_post_page()
        before_comment_value = self.dynamic.get_comment_value()
        if before_comment_value == "评论":
            self.dynamic.click_to_comment_page()
            self.dynamic.edit_comment()
            self.dynamic.press_comment_btn()
            after_comment_value = self.dynamic.get_comment_value()
            self.dynamic.save_screenshots("社区tab帖子评论功能截图")
            self.logInfo.logEnd("社区tab帖子评论功能日志")
            assert after_comment_value == '1'
        else:
            before_comment_value = int(before_comment_value)
            self.dynamic.click_to_comment_page()
            self.dynamic.edit_comment()
            self.dynamic.press_comment_btn()
            after_comment_value = int(self.dynamic.get_comment_value())
            assert after_comment_value == before_comment_value + 1

    @allure.story("个人主页-动态tab下帖子删除功能测试")
    @pytest.mark.smoke
    def test_dynamic_delete_post(self):
        """
        测试社区删帖功能
        :return:删帖前当前帖子发布者名称与删帖后贴子发布者名称不同即为pass
        """
        now_my_dynamic_num = int(self.dynamic.get_my_dynamic_num_value())
        time.sleep(2)
        before_dynamic_index = self.dynamic.get_my_dynamic_index()

        self.dynamic.to_post_page()
        if now_my_dynamic_num == 1:
            self.dynamic.click_share_btn()
            self.dynamic.click_delete_btn()
            self.dynamic.click_confirm_delete_btn()
            after_dynamic_index = self.dynamic.get_my_dynamic_index()
            self.dynamic.save_screenshots("社区tab帖子删除功能截图")
            self.logInfo.logEnd("社区tab帖子删除功能日志")
            assert len(before_dynamic_index) == 1 and after_dynamic_index is None
        else:
            now_publisher_name = self.dynamic.get_publisher_name()
            self.dynamic.click_share_btn()
            self.dynamic.click_delete_btn()
            self.dynamic.click_confirm_delete_btn()
            after_publisher_name = self.dynamic.get_publisher_name()
            self.dynamic.save_screenshots("社区tab帖子删除功能截图")
            self.logInfo.logEnd("社区tab帖子删除功能日志")
            assert now_publisher_name != after_publisher_name

    @classmethod
    def teardown_class(cls):
        cls.dynamic.driver.quit()
