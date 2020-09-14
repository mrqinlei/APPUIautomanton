# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest
import os


@allure.feature("社区测试内容")
class TestCommunityPost:

    @classmethod
    def setup_class(cls):
        cls.community_post = BaseDriver.andriod_driver().to_community_tab()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是用户类")
        # self.user_page.get_device_state_custom()
        # community_icon = self.community_post.get_community_icon()
        # if community_icon is None:
        #     self.community_post = BaseDriver.andriod_driver().to_community_tab()
        # else:
        #     pass
        self.logInfo = LogInfo()

    @pytest.mark.todisplay
    @pytest.mark.smoke
    def test_publish_post(self):
        """
        测试社区发帖功能
        :return: 获取的成功发布toast即为通过
        """
        self.community_post.to_publish_post()
        judge_have_diary_auth = self.community_post.judge_have_diary_authority()
        if judge_have_diary_auth is not None:
            self.community_post.to_select_post_btn()
            self.community_post.to_select_photo_btn()
            self.community_post.click_next_btn()
            self.community_post.click_next_step()
            self.community_post.click_and_input_post_content()
            self.community_post.click_publish_btn()
            get_toast = self.community_post.find_publish_success_toast()
            self.community_post.save_screenshots("社区tab发布帖子功能截图")
            self.logInfo.logEnd("社区tab发布帖子功能日志")
            assert get_toast == '发布成功'
        else:
            self.community_post.to_select_photo_btn()
            self.community_post.click_next_btn()
            self.community_post.click_next_step()
            self.community_post.click_and_input_post_content()
            self.community_post.click_publish_btn()
            get_toast = self.community_post.find_publish_success_toast()
            self.community_post.save_screenshots("社区tab发布帖子功能截图")
            self.logInfo.logEnd("社区tab发布帖子功能日志")
            assert get_toast == '发布成功'


    @pytest.mark.smoke
    def test_like_post(self):
        """
        测试对社区帖子进行点赞
        :return:若帖子点赞数为0则点赞后数量为1，若>0,则点赞后结果加一，或取消点赞，结果减一
        """
        self.community_post.to_search_user_by_id()
        self.community_post.click_search_box()
        self.community_post.click_search_box()
        self.community_post.click_search_history()
        self.community_post.click_user_tab()
        self.community_post.click_to_user_page()
        self.community_post.click_to_post_content()
        before_press_like_btn = self.community_post.get_like_btn_value()
        if before_press_like_btn == "点赞":
            self.community_post.click_like_btn()
            after_press_like_btn = self.community_post.get_like_btn_value()
            self.community_post.save_screenshots("社区tab帖子点赞功能截图")
            self.logInfo.logEnd("社区tab帖子点赞功能日志")
            assert after_press_like_btn == '1'
        else:
            before_press_like_btn = int(before_press_like_btn)
            self.community_post.save_screenshots("社区tab帖子点赞功能截图")
            self.logInfo.logEnd("社区tab帖子点赞功能日志")
            self.community_post.click_like_btn()
            after_press_like_btn = int(self.community_post.get_like_btn_value())
            assert after_press_like_btn == before_press_like_btn + 1 \
                   or after_press_like_btn == before_press_like_btn - 1

    @pytest.mark.smoke
    def test_comment_post(self):
        """
        测试对帖子评论功能
        :return:帖子评论数为0时，评论后返回结果为1，或当前评论数>1时，返回结果为评论数+1即为通过
        """
        self.community_post.to_search_user_by_id()
        self.community_post.click_search_box()
        self.community_post.click_search_box()
        self.community_post.click_search_history()
        self.community_post.click_user_tab()
        self.community_post.click_to_user_page()
        self.community_post.click_to_post_content()
        before_comment_value = self.community_post.get_comment_value()
        if before_comment_value == "评论":
            self.community_post.click_to_comment_page()
            self.community_post.edit_comment()
            self.community_post.press_comment_btn()
            after_comment_value = self.community_post.get_comment_value()
            self.community_post.save_screenshots("社区tab帖子评论功能截图")
            self.logInfo.logEnd("社区tab帖子评论功能日志")
            assert after_comment_value == '1'
        else:
            before_comment_value = int(before_comment_value)
            self.community_post.click_to_comment_page()
            self.community_post.edit_comment()
            self.community_post.press_comment_btn()
            after_comment_value = int(self.community_post.get_comment_value())
            assert after_comment_value == before_comment_value + 1

    @pytest.mark.smoke
    def test_delete_post(self):
        """
        测试社区删帖功能
        :return:删帖前当前帖子发布者名称与删帖后贴子发布者名称不同即为pass
        """
        self.community_post.to_search_user_by_id()
        self.community_post.click_search_box()
        self.community_post.click_search_box()
        self.community_post.click_search_history()
        self.community_post.click_user_tab()
        self.community_post.click_to_user_page()
        self.community_post.click_to_post_content()
        now_publisher_name = self.community_post.get_publisher_name()
        self.community_post.click_share_btn()
        self.community_post.click_delete_btn()
        self.community_post.click_confirm_delete_btn()
        after_publisher_name = self.community_post.get_publisher_name()
        self.community_post.save_screenshots("社区tab帖子删除功能截图")
        self.logInfo.logEnd("社区tab帖子删除功能日志")
        assert now_publisher_name != after_publisher_name

    @classmethod
    def teardown_class(cls):
        cls.community_post.driver.quit()
