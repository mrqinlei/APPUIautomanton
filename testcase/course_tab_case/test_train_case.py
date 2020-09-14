# -*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
import pytest


@allure.feature("测试参加训练课程模块")
class TestJoinTrain:
    """
    训练课程模块测试
    """

    def setup_class(cls):
        cls.join_train = BaseDriver.andriod_driver().to_train_page()

    def setup(self):
        # sport_icon = self..get_sport_icon()
        # if sport_icon is None:
        #     self.sport_page.driver.quit()
        #     time.sleep(3)
        #     self.sport_page = BaseDriver.andriod_driver().to_heart_rate_page()
        # else:
        #     pass
        self.logInfo = LogInfo()

    @allure.story("判断是否已参加训练课程")
    @allure.severity('Normal')
    @pytest.mark.smoke
    # @pytest.mark.dependency()
    @pytest.mark.run(order=1)
    def test_judge_already_join_train(self):
        """
        判断是否已有参加课程 若有则退出课程
        :return:
        """
        judge_join_train = self.join_train.judge_if_already_join_train()
        if judge_join_train is not None:
            self.join_train.click_continue_train()
            train_flag = True
            while train_flag == True:
                if self.join_train.get_more_btn() is not None:
                    self.join_train.click_more_btn()
                    self.join_train.click_exit_train()
                    self.join_train.click_confirm_exit_train_btn()
                else:
                    train_flag = False
            after_exit_judge = self.join_train.judge_if_already_join_train()
        else:
            after_exit_judge = self.join_train.judge_if_already_join_train()
        assert after_exit_judge is None

    @allure.story("参加训练课程观看并退出观看")
    @allure.severity('Normal')
    @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["test_judge_already_join_train"])
    @pytest.mark.run(order=2)
    def test_join_train(self):
        """
        添加训练课程，观看并退出
        :return: 课程进入前后课程名称一致，并且播放成功即为通过
        """
        self.join_train.click_join_train()
        self.join_train.click_select_train_target()
        self.join_train.click_next_step()
        self.join_train.click_select_train_level()
        self.join_train.click_next_step()
        self.join_train.click_select_start_date()
        self.join_train.click_next_step()
        time.sleep(3)
        before_train_name = self.join_train.get_train_name()
        self.join_train.click_join_train_btn()
        after_train_name = self.join_train.get_train_name()
        self.join_train.click_start_train()
        already_download_judge = self.join_train.judge_already_download_video()
        if already_download_judge is not None:
            self.join_train.click_download_today_video()
            time.sleep(10)
            video_play_judge = self.join_train.video_play_surface_judge()
            self.join_train.touch_video()
            self.join_train.click_close_video_btn()
            self.join_train.confirm_close_video()
        elif already_download_judge is None:
            video_play_judge = self.join_train.video_play_surface_judge()
            self.join_train.touch_video()
            self.join_train.click_close_video_btn()
            self.join_train.confirm_close_video()
        self.join_train.save_screenshots("课程tab初次参加训练截图")
        self.logInfo.logEnd("课程tab初次参加训练日志")
        assert before_train_name == after_train_name and video_play_judge is not None

    @allure.story("退出训练课程")
    @allure.severity('Normal')
    @pytest.mark.smoke
    def test_exit_train(self):
        """
        退出训练课程
        :return:
        """
        self.join_train.click_continue_train()
        self.join_train.click_more_btn()
        self.join_train.click_exit_train()
        self.join_train.click_confirm_exit_train_btn()
        self.join_train.save_screenshots("课程tab退出训练截图")
        self.logInfo.logEnd("课程tab退出训练日志")
        exit_train_result = self.join_train.get_exit_train_result_element()
        assert exit_train_result is not None

    @classmethod
    def teardown_class(cls):
        # cls.join_train.click_back_by_native(type='back')
        cls.join_train.driver.quit()
