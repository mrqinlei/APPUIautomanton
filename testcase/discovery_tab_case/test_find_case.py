from base.base_driver import BaseDriver
from selenium.webdriver.remote.webdriver import WebDriver
import time
import allure
from utils.log_info import LogInfo
import pytest

@allure.feature("发现模块测试内容")
class TestFindCase:

    @classmethod
    def setup_class(cls):
        cls.find_page = BaseDriver.andriod_driver().to_find_page()
        # cls.logInfo = LogInfo()
        time.sleep(3)

    def setup(self):
        activities_icon = self.find_page.get_activity_icon()
        if activities_icon is None:
            self.find_page = BaseDriver.andriod_driver().to_find_page()
        else:
            pass
        self.logInfo = LogInfo()


    @allure.story("切换到活动页面测试")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    def test_click_activity_btn(self):
        '''
        进入到活动页面
        :return: 是否成功进入活动页面
        '''
        self.find_page.click_activity_btn()
        title = self.find_page.get_my_participation_title()
        self.find_page.save_screenshots("活动页面截图")
        self.logInfo.logEnd("进入活动页面日志")
        self.find_page.click_back_by_native(type="find")
        assert title == '我参与的'


    @allure.story("进入资讯页面测试")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    def test_news(self):
        """
        进入资讯页面
        :return:  是否成功进入资讯页面
        """
        self.find_page.click_news()
        title = self.find_page.get_news_icon_page_title()
        self.find_page.save_screenshots("资讯页面截图")
        self.logInfo.logEnd("进入资讯页面日志")
        self.find_page.click_back_by_native(type="find")
        assert title == '全部资讯'

    @allure.story("进入健康服务页面测试")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    def test_health_service(self):
        '''
        点击健康服务icon
        :return: 是否成功进入到健康服务页面
        '''
        self.find_page.click_health_service()
        title = self.find_page.get_health_service_title()
        self.find_page.save_screenshots("健康服务截图")
        self.logInfo.logEnd("点击健康服务更多按钮日志")
        self.find_page.click_back_by_native(type="find")
        assert title == "健康服务"


    @allure.story("获取发现页面是否有热门活动模块")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    @pytest.mark.dependency()
    def test_get_activities(self):
        '''
        获取发现页面是否有热门活动
        :return:有热门活动 返回True
        '''
        title = self.find_page.get_activities_title()
        self.find_page.save_screenshots("判断发现页面是否有热门活动截图")
        self.logInfo.logEnd("判断发现页面是否有热门活动日志")
        assert title is not None


    @allure.story("热门活动跳转测试")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    @pytest.mark.dependency(depends=['TestFindCase::test_get_activities'])
    def test_click_popular_activities(self):
        '''
        点击热门活动
        :return:是否成功跳转到活动页面
        '''
        self.find_page.click_popular_activities()
        title = self.find_page.get_activities_title()
        self.find_page.save_screenshots("热门活动截图")
        self.logInfo.logEnd("点击热门活动日志")
        self.find_page.click_back_by_native(type="left")
        assert title == "中国节·庚子端午"


    @allure.story("进入发现首页热门资讯文章详情页")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    def test_news_page(self):
        '''
        进入热门资讯详情页
        :return: 是否成功进入发现页面热门资讯文章详情页
        '''
        news_title = self.find_page.get_news_title()
        if news_title is None:
            news_title = self.find_page.get_news_title_2()
            self.find_page.click_news_layout_2()
        else:
            self.find_page.click_news_layout()
        news_page_title = self.find_page.get_news_page_title()
        # self.find_page.click_news_back_to_find()
        self.find_page.save_screenshots("热门资讯详情页截图")
        self.logInfo.logEnd("进入热门资讯日志")
        self.find_page.click_back_by_native(type="left")
        assert news_title == news_page_title

    @allure.story("进入内容推荐页面测试")
    @allure.severity('Blocker')
    @pytest.mark.discoveryP0
    @pytest.mark.core
    def test_click_content_recommendation_first(self):
        '''
        进入到发现页面内容推荐列表里第一个帖子详情页面
        :return: 是否成功进入对应帖子的页面
        '''
        time.sleep(3)
        # self.find_page.swipe_on("up_middle")
        title = self.find_page.get_content_recommendation_first_title()
        self.find_page.click_content_recommendation_first_layout()
        first_title = self.find_page.get_content_recommendation_first_page_title()
        # self.find_page.click_news_back_to_find()
        self.find_page.save_screenshots("内容推荐列表第一个帖子详情页截图")
        self.logInfo.logEnd("进入内容推荐列表第一个帖子详情页面日志")
        self.find_page.click_back_by_native(type="left")
        assert title == first_title


    @classmethod
    def teardown_class(cls):
        cls.find_page.driver.quit()
