#-*- coding: utf-8 -*-

from base.base_page import BasePage

class FriendsPage(BasePage):


    def get_first_friend_name(self):
        return self.find_element_and_value("first_name", "friends_page_element")

    def get_first_friend_steps(self):
        return self.find_element_and_value("first_steps", "friends_page_element")

    def get_first_friend_sleep(self):
        return self.find_element_and_value("first_sleep", "friends_page_element")

    def get_first_friend_weight(self):
        return self.find_element_and_value("first_weight", "friends_page_element")

    def click_first_friend_layout(self):
        self.find_element_and_click("first_friend", "friends_page_element")

    def get_person_name(self):
        return self.find_element_and_value("person_title", "friends_page_element")

    def get_person_steps(self):
        return self.find_element_and_value("person_steps", "friends_page_element")

    def get_person_sleep(self):
        return self.find_element_and_value("person_sleep", "friends_page_element")

    def get_person_weight(self):
        return self.find_element_and_value("person_weight", "friends_page_element")

    def get_friend_icon(self):
        return self.find_element("friend_layout", "mine_page_element")




