from base.base_page import BasePage

class FindPage(BasePage):

    # def click_find_btn(self):
    #     self.find_element_and_click("find_tab","find_page_element")

    #点击发现页面热门活动卡片
    def click_popular_activities(self):
        self.find_element_and_click("popular_activities", "find_page_element")

    #获取发现页面热门活动详情页标题
    def get_activities_title(self):
        return self.find_element_and_value("activities_title", "find_page_element")

    # 点击轮播图
    def click_rotation_chart(self):
        self.find_element_and_click("rotation_chart", "find_page_element")


    def click_more_btn(self):  #点击健康服务 更多按钮
        self.find_element_and_click("more_btn", "find_page_element")

    #获取健康服务详情页标题
    def get_health_service_title(self):
        return self.find_element_and_value("health_service_title", "find_page_element")

    # def click_mall_btn(self): #点击商城
    #     return self.find_element_and_value("", "")

    def click_serve_btn(self): #点击服务
        self.find_element_and_click("serve_btn", "find_page_element")

    def get_hot_recommend_title(self):#获取热门推荐text属性
        return self.find_element_and_value("hot_recommend_title", "find_page_element")

    def click_activity_btn(self):#点击活动
        self.find_element_and_click("activity_btn", "find_page_element")

    def get_my_participation_title(self):
        return self.find_element_and_value("my_participation_title", "find_page_element")


    def click_midong_ring(self): #进入米动圈
        self.find_element_and_click("midong_ring", "find_page_element")

    def get_midong_ring_title(self):
        return self.find_element_and_value("midong_ring_title", "find_page_element")

    #点击健康服务
    def click_health_service(self):
        self.find_element_and_click("health_service_layout", "find_page_element")

    #点击资讯
    def click_news(self):
        self.find_element_and_click("news_layout", "find_page_element")

    #得到资讯的标题
    def get_news_icon_page_title(self):
        return self.find_element_and_value("news_title", "find_page_element")

    #得到发现页面热门资讯卡片的标题
    def get_news_title(self):
        return self.find_element_and_value("find_news_title", "find_page_element")

    #点击发现页面热门资讯卡片
    def click_news_layout(self):
        self.find_element_and_click("find_news_layout", "find_page_element")

    #得到没有热门活动时热门咨询卡片的标题
    def get_news_title_2(self):
        return self.find_element_and_value("find_news_title_2", "find_page_element")

    # 点击没有热门活动时热门资讯卡片
    def click_news_layout_2(self):
        self.find_element_and_click("find_news_layout_2", "find_page_element")

    #得到热门资讯详情页的标题
    def get_news_page_title(self):
        return self.find_element_and_value("news_page_title", "find_page_element")

    #资讯详情页点击返回按钮
    def click_news_back_to_find(self):
        self.find_element_and_click("news_page_back", "find_page_element")

    #获取内容推荐列表第一个帖子标题
    def get_content_recommendation_first_title(self):
        return self.find_element_and_value("content_recommendation_first_title", "find_page_element")

    #点击内容推荐列表第一个帖子
    def click_content_recommendation_first_layout(self):
        self.find_element_and_click("content_recommendation_first_layout", "find_page_element")

    #获得内容推荐列表第一个帖子详情页的标题
    def get_content_recommendation_first_page_title(self):
        return self.find_element_and_value("content_recommendation_first_page_title", "find_page_element")

    def get_activity_icon(self):
        return self.find_element("activity_btn", "find_page_element")