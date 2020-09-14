#-*- coding: utf-8 -*-
from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo

@allure.feature("社区模块-搜索测试内容")
class TestSearchCase:

    # def setup(self):
    #     self.search = BaseDriver.andriod_driver().to_mine_collect_page()
    #     self.logInfo = LogInfo()
    #
    # @allure.story("我的收藏-帖子tab下帖子详情页测试")
    # @allure.severity('critical')
    # @allure.issue('http://www.baidu.com', '问题')
    # @allure.testcase('http://www.sina.com', '测试用例')
    # def test_collect_post_page(self):
    #     """
    #     跳转帖子tab下帖子详情页
    #     :return: 是否成功跳转到帖子详情页面
    #     """
    #     time.sleep(3)
    #     first_name = self.collect.get_first_post_name()
    #     self.collect.to_first_post_page()
    #     second_name = self.collect.get_publisher_name()
    #     self.collect.save_screenshots("查看跳转帖子tab下帖子详情页截图")
    #     self.logInfo.logEnd("查看帖子tab下帖子详情页日志")
    #     assert first_name == second_name
    pass



    def teardown(self):
        self.search.driver.quit()