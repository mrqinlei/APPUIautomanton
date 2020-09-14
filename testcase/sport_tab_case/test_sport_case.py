#-*- coding: utf-8 -*-

from base.base_driver import BaseDriver
import time
import allure
from utils.log_info import LogInfo
from utils.string_edit import del_symbol, del_str
import pytest

@allure.feature("运动模块测试内容")
class TestSportCase:


    @classmethod
    def setup_class(cls):
        cls.sport_page = BaseDriver.andriod_driver().to_sport_page()
        # cls.logInfo = LogInfo()

    def setup(self):
        # print ("这是运动类")
        # self.sport_page.get_device_state_custom()
        sport_icon = self.sport_page.get_sport_icon()
        if sport_icon is None:
            self.sport_page.driver.quit()
            time.sleep(3)
            self.sport_page = BaseDriver.andriod_driver().to_sport_page()
        else:
            pass
        self.logInfo = LogInfo()



    @allure.story("首页点击步数进入今日步数页面测试")
    @allure.severity('Blocker')
    # @allure.issue('http://www.baidu.com',"问题")
    # @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.sportP0
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.smoke
    def test_steps_page(self):
        """
        测试从首页点击步数，进入今日详情页，对两侧步数是否一致进行验证
        :return: 两侧数据一致时，代表PASS
        """
        steps_nums = self.sport_page.get_steps_main_page()
        steps_num = int(del_symbol(steps_nums))
        if steps_num > 0:
            self.sport_page.click_steps_layout()
            steps = int(self.sport_page.get_steps_today())
            isSuccess = (steps_num == steps)
        else:
            #此时没有产生步数,不知道文案，暂时标为失败
            isSuccess = False
        self.sport_page.save_screenshots("进入今日步数详情页截图")
        self.logInfo.logEnd("进入今日步数详情页日志")
        self.sport_page.click_back_by_native("left_btn")
        assert isSuccess is True


    # @allure.story("首页点击睡眠卡片进入昨晚睡眠页面测试")
    # @allure.severity('Blocker')
    # def test_last_sleep_time(self):
    #     """
    #     测试从首页点击昨晚睡眠长卡片，进入昨晚睡眠页面，对两侧睡眠时长是否一致进行验证
    #     :return: 两侧数值一致时，PASS
    #     """
    #     sleep_time_mian_page = self.sport_page.get_sleep_time_main_page()
    #     sleep_before = sleep_time_mian_page.split(" ")[1]
    #     self.sport_page.click_first_layout()
    #     sleep_time_mine_page = self.sport_page.get_sleep_time_mine()
    #     # sleep_middle = del_symbol(sleep_time_mine_page)
    #     # sleep_after = del_str(sleep_middle, " ")
    #     self.sport_page.save_screenshots("从首页点击睡眠卡片进入昨晚睡眠截图")
    #     self.logInfo.logEnd("从首页点击睡眠卡片进入昨晚睡眠日志")
    #     self.sport_page.click_back_by_native("left_btn")
    #     assert sleep_before == sleep_time_mine_page


    @allure.story("首页点击体重卡片进入体重详情页面测试")
    @allure.severity('Blocker')
    # @allure.issue('http://www.baidu.com',"问题")
    # @allure.testcase('http://www.sina.com', '测试用例')
    @pytest.mark.sportP0
    @pytest.mark.core
    @pytest.mark.release
    # @pytest.mark.smoke  #首页布局不固定，当前账号暂不修改布局
    @pytest.mark.skip   #首页布局原因
    def test_weight(self):
        """
        测试从首页点击体重卡片，进入体重详情页，对两侧数值是否一致进行验证
        :return:两侧数值一致时，PASS
        """
        weight_main_page = self.sport_page.get_weight_main_page()
        weight_temp = weight_main_page.split(" ")[1]
        # self.sport_page.to_mine_status_page()
        self.sport_page.click_weight_layout()
        weight_mine_page = self.sport_page.get_weight_mine_page() + "斤"
        self.sport_page.save_screenshots("进入体重详情页截图")
        self.logInfo.logEnd("进入体重详情页日志")
        self.sport_page.click_back_by_native("left_btn")
        assert weight_temp == weight_mine_page

    @allure.story("进行健走测试")
    @allure.severity('Blocker')
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.smoke
    @pytest.mark.sportP0
    def test_work_page(self):
        temp = self.sport_page.to_work_page()
        self.sport_page.save_screenshots("进行健走截图")
        self.logInfo.logEnd("进行健走日志")
        assert temp is True

    @allure.story("进行室外跑测试")
    @allure.severity('Blocker')
    @pytest.mark.core
    @pytest.mark.release
    @pytest.mark.smoke
    @pytest.mark.sportP0
    def test_outdoor_run_page(self):
        temp = self.sport_page.to_run_outdoor_page()
        self.sport_page.save_screenshots("进行室外跑截图")
        self.logInfo.logEnd("进行室外跑日志")
        assert temp is True

    @allure.story("进行室内跑测试")
    @allure.severity('Blocker')
    @pytest.mark.core
    @pytest.mark.release
    # @pytest.mark.smoke   #元素未找到
    @pytest.mark.sportP0
    def test_indoor_run_page(self):
        temp = self.sport_page.to_run_indoor_page()
        self.sport_page.save_screenshots("进行室内跑截图")
        self.logInfo.logEnd("进行室内跑日志")
        assert temp is True

    @allure.story("进行骑行测试")
    @allure.severity('Blocker')
    @pytest.mark.core
    @pytest.mark.release
    # @pytest.mark.smoke   #元素未找到
    @pytest.mark.sportP0
    def test_cycling_page(self):
        temp = self.sport_page.to_cycling_page()
        self.sport_page.save_screenshots("进行骑行截图")
        self.logInfo.logEnd("进行骑行日志")
        assert temp is True

    @allure.story("查找运动tab页广告位")
    @allure.severity('Normal')
    @pytest.mark.dependency()
    @pytest.mark.sportNormal
    def test_find_ad(self):
        self.sport_page.to_status_page()
        # 获取广告控件
        if self.sport_page.get_ad_element() is None:
            is_have_ad = False
        else:
            is_have_ad = True
        assert is_have_ad is True

    @allure.story("进入首页广告页测试")
    @allure.severity('Normal')
    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    @pytest.mark.dependency(depends=['TestSportCase::test_find_ad'])
    @pytest.mark.sportNormal
    def test_ad_page(self):
        self.sport_page.to_advertisement_page()
        time.sleep(2)
        back_btn = self.sport_page.get_back_btn()
        ad_back_btn = self.sport_page.get_ad_back_btn()
        self.sport_page.save_screenshots("进入首页广告截图")
        self.logInfo.logEnd("进入首页广告日志")
        if back_btn is not None:
            self.sport_page.click_back_btn()
        else:
            self.sport_page.click_back_by_native(type="back")
        assert back_btn is not None or ad_back_btn is not None

    @allure.story("进入首页大家都在练-长卡片测试")
    @allure.severity('Normal')
    @pytest.mark.dependency()
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @pytest.mark.sportNormal
    def test_practice_long_card(self):
        time.sleep(5)
        self.sport_page.swipe_on("up_middle")
        self.sport_page.to_practice_long_card()
        back_btn = self.sport_page.get_classic_back_btn()
        time.sleep(2)
        self.sport_page.save_screenshots("进入首页大家都在练长卡片截图")
        self.logInfo.logEnd("进入首页大家都在练长卡片日志")
        self.sport_page.click_classic_back_btn()
        assert back_btn is not None

    @allure.story("进入首页大家都在练-短卡片1测试")
    @allure.severity('Normal')
    @pytest.mark.dependency(depends=["TestSportCase::test_practice_long_card"])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @pytest.mark.sportNormal
    def test_practice_short_card_1(self):
        time.sleep(5)
        self.sport_page.swipe_on("up_middle")
        self.sport_page.to_practice_short_card_1()
        back_btn = self.sport_page.get_classic_back_btn()
        time.sleep(2)
        self.sport_page.save_screenshots("进入首页大家都在练-短卡片1截图")
        self.logInfo.logEnd("进入首页大家都在练-短卡片1日志")
        self.sport_page.click_classic_back_btn()
        assert back_btn is not None

    @allure.story("进入首页大家都在练-短卡片2测试")
    @allure.severity('Normal')
    @pytest.mark.dependency(depends=["TestSportCase::test_practice_short_card_1"])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @pytest.mark.sportNormal
    def test_practice_short_card_2(self):
        # time.sleep(5)
        # self.sport_page.swipe_on("up_middle")
        self.sport_page.to_practice_short_card_2()
        back_btn = self.sport_page.get_classic_back_btn()
        time.sleep(2)
        self.sport_page.save_screenshots("进入首页大家都在练-短卡片2截图")
        self.logInfo.logEnd("进入首页大家都在练-短卡片2日志")
        self.sport_page.click_classic_back_btn()
        assert back_btn is not None


    @pytest.mark.skip(reason="暂时没有赛事活动模块")
    @allure.story("进入首页赛事活动页面测试")
    @allure.severity('Normal')
    @pytest.mark.sportNormal
    def test_premitition_page(self):
        # time.sleep(5)
        # self.sport_page.swipe_on("up_middle")
        # time.sleep(3)
        # self.sport_page.swipe_on("up_middle")
        self.sport_page.to_competition_activity_page()
        back_btn = self.sport_page.get_back_btn()
        time.sleep(5)
        self.sport_page.save_screenshots("进入首页赛事活动页面截图")
        self.logInfo.logEnd("进入首页赛事活动页面日志")
        self.sport_page.click_back_btn()
        assert back_btn is not None

    # @allure.story("进入首页热门话题第一部分详情页测试")
    # @allure.severity('Normal')
    # def test_hot_topic_first_page(self):
    #     time.sleep(5)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     # nick_element = self.sport_page.get_nick_element()
    #     # self.sport_page.find_element_to_element(nick_element)
    #     nick_name = self.sport_page.get_hot_topic_nick_name()
    #     self.sport_page.to_hot_topic_first_card()
    #     nick_name_page = self.sport_page.get_topic_page_nick_name()
    #     time.sleep(3)
    #     self.sport_page.save_screenshots("进入首页热门话题第一部分详情页截图")
    #     self.logInfo.logEnd("进入首页热门话题第一部分详情页日志")
    #     assert nick_name == nick_name_page
    #
    # @allure.story("进入首页热门话题第二部分详情页测试")
    # @allure.severity('Normal')
    # def test_hot_topic_second_page(self):
    #     time.sleep(5)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     # nick_element = self.sport_page.get_nick_element()
    #     # self.sport_page.find_element_to_element(nick_element)
    #     nick_name = self.sport_page.get_second_nick_name()
    #     self.sport_page.to_hot_topic_second_card()
    #     nick_name_page = self.sport_page.get_topic_page_nick_name()
    #     time.sleep(3)
    #     self.sport_page.save_screenshots("进入首页热门话题第二部分详情页截图")
    #     self.logInfo.logEnd("进入首页热门话题第二部分详情页日志")
    #     assert nick_name == nick_name_page
    #
    # @allure.story("进入首页热门话题第三部分详情页测试")
    # @allure.severity('Normal')
    # def test_hot_topic_third_page(self):
    #     time.sleep(5)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     time.sleep(2)
    #     self.sport_page.swipe_on("up_middle")
    #     # nick_element = self.sport_page.get_nick_element()
    #     # self.sport_page.find_element_to_element(nick_element)
    #     nick_name = self.sport_page.get_third_nick_name()
    #     self.sport_page.to_hot_topic_third_card()
    #     nick_name_page = self.sport_page.get_topic_page_nick_name()
    #     time.sleep(3)
    #     self.sport_page.save_screenshots("进入首页热门话题第三部分详情页截图")
    #     self.logInfo.logEnd("进入首页热门话题第三部分详情页日志")
    #     assert nick_name == nick_name_page



    @classmethod
    def teardown_class(cls):
        cls.sport_page.driver.quit()
