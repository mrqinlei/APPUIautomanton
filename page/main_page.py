# -*- coding: utf-8 -*-

from base.base_page import BasePage
from page.community_tab_page.other_country_user_page import OtherCountryUserPage
from page.community_tab_page.posted_message_page import PostedMessagePage
from page.course_tab_page.train_page import CourseTrainPage
from page.login_register_page.login_page import LoginPage
from page.mine_tab_page.message_page import MessagePage
from page.mine_tab_page.my_dynamic_page import MyDynamicPage
from page.mine_tab_page.my_equipment_page import MyEquipmentPage
from page.mine_tab_page.user_page import UserPage
from page.sport_tab_page.energy_page import EnergyPage
from page.sport_tab_page.my_sports_page import MySportsPage
from page.sport_tab_page.my_status_page import MyStatusPage
from page.sport_tab_page.mystatus_to_sleep_page import MyStatusSleepPage
from page.sport_tab_page.sport_page import SportPage
from page.sport_tab_page.mine_sport_page import MineSportPage
from page.sport_tab_page.today_steps_page import TodayStepsPage
from page.sport_tab_page.sleep_page import SleepPage
from page.mine_tab_page.user_info_page import UserInfoPage
from page.mine_tab_page.personal_homepage_page import PersonalHomepagePage
from page.mine_tab_page.friends_page import FriendsPage
from page.mine_tab_page.course_page import CoursePage
from page.mine_tab_page.collect_page import CollectPage
from page.sport_tab_page.heart_rate_page import HeartRatePage
from page.sport_tab_page.weight_page import WeightPage

from page.z_find_tab_page.find_page import FindPage
from page.community_tab_page.search_page import SearchPage


class MainPage(BasePage):

    # def to_community_page(self):
    #     self.find_element("community_tab", "main_page_element")
    #     return CommunityPage()

    def to_login_page(self):
        return LoginPage(self.driver)

    def to_sport_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        return SportPage(self.driver)

    def to_mine_sport_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("more_btn", "main_page_element")
        self.find_element_and_click("mine_sport_tab", "status_page_element")
        return MineSportPage(self.driver)

    def to_today_steps_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("steps_number", "main_page_element")
        return TodayStepsPage(self.driver)

    def to_sleep_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("sleep_layout", "main_page_element")
        return SleepPage(self.driver)

    def to_heart_rate_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        return HeartRatePage(self.driver)

    def to_weight_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        return WeightPage(self.driver)

    def to_weight_page(self):
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("more_btn", "main_page_element")
        self.find_element_and_click("mine_sport_tab", "status_page_element")
        return EnergyPage(self.driver)

    def to_mine_page(self):
        self.find_element_and_click("mine_tab", "main_page_element")
        return MessagePage(self.driver)

    def to_mine_page_user(self):
        # 跳转到我的页面
        self.find_element_and_click("mine_tab", "main_page_element")
        return UserPage(self.driver)

    def to_mine_user_page(self):
        # 跳转到我的-个人信息页面
        self.find_element_and_click("mine_tab", "main_page_element")
        self.find_element_and_click("mine_person_img", "mine_page_element")
        return UserInfoPage(self.driver)

    def to_mine_personal_homepage(self):
        # 跳转到我的-个人主页
        self.find_element_and_click("mine_tab", "main_page_element")
        self.find_element_and_click("mine_dynamic", "mine_page_element")
        return PersonalHomepagePage(self.driver)

    def to_mine_friends_page(self):
        # 跳转到我的-亲友页面
        self.find_element_and_click("mine_tab", "main_page_element")
        self.swipe_on('up')
        self.find_element_and_click("friend_layout", "mine_page_element")
        return FriendsPage(self.driver)

    def to_mine_course_page(self):
        # 跳转到我的-我的课程
        self.find_element_and_click("mine_tab", "main_page_element")
        self.find_element_and_click("mine_course", "mine_page_element")
        return CoursePage(self.driver)

    def to_mine_collect_page(self):
        # 跳转到我的-我的收藏
        self.find_element_and_click("mine_tab", "main_page_element")
        self.find_element_and_click("mine_favorite", "mine_page_element")
        return CollectPage(self.driver)

    def to_find_page(self):
        self.find_element_and_click("find_tab", "find_page_element")
        return FindPage(self.driver)

    def to_search_page(self):
        # 跳转到社区-发现页面
        self.find_element_and_click("descovery_tab", "main_page_element")
        return SearchPage(self.driver)

    def to_my_status_page(self):
        # 跳转到运动-我的状态页面
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("more_btn", "main_page_element")
        return MyStatusPage(self.driver)

    def to_my_status_sleep_page(self):
        # 跳转到运动-我的状态-昨晚睡眠页面
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("more_btn", "main_page_element")
        self.find_element_and_click("before_sleep_time", "my_status_page_element")
        return MyStatusSleepPage(self.driver)

    def to_my_sports_page(self):
        # 跳转到运动-我的状态页面
        self.find_element_and_click("sport_tab", "main_page_element")
        self.find_element_and_click("more_btn", "main_page_element")
        self.find_element_and_click("mine_sport_tab", "status_page_element")
        return MySportsPage(self.driver)

    def to_train_page(self):
        # 跳转到课程tab-开始训练计划
        self.find_element_and_click("classes_tab","main_page_element")
        # self.find_element_and_click("into_train_page","course_page_element")
        return CourseTrainPage(self.driver)

    def to_other_country_workout_tab(self):
        # 系统语言英文跳转到workout_tab
        return OtherCountryUserPage(self.driver)

    def to_community_tab(self):
        #跳转到社区页面
        self.find_element_and_click("community_tab","main_page_element")
        return PostedMessagePage(self.driver)

    def to_my_dynamic_page(self):
        #跳转到我的tab下我的动态页面
        self.find_element_and_click("mine_tab","main_page_element")
        self.find_element_and_click("mine_dynamic","mine_page_element")
        return MyDynamicPage(self.driver)

    def to_mine_equipment_page(self):
        #跳转到我的tab下 我的设备页面
        self.find_element_and_click("mine_tab","main_page_element")
        self.find_element_and_click("mine_equipment","mine_equipment_element")
        return MyEquipmentPage(self.driver)




    # def register_by_phone(self):
    #     self.find_element_and_click("register_btn",  "login_page_element")
