from base.base_page import BasePage


class SportPage(BasePage):

    def get_sleep_time_main_page(self):
        return self.find_element_and_value("last_sleep", "main_page_element")

    def click_first_layout(self):
        self.find_element_and_click("sleep_layout", "main_page_element")

    def get_sleep_time_mine(self):
        return self.find_element_and_value("sleep_time", "sleep_page_element")

    def get_sleep_time_mine_page(self):
        return self.find_element_and_value("last_night", "status_page_element")
        # deep_sleep = self.find_element_and_value("deep_sleep", "status_page_element")
        # light_sleep = self.find_element_and_value("light_sleep", "status_page_element")
        # sober = self.find_element_and_value("sober", "status_page_element")
        # self.find_element_and_click("last_night", "status_page_element")
        # title_3 = self.find_element_and_value("")


    def to_mine_status_page(self):
        self.find_element_and_click("more_btn", "main_page_element")

    def get_weight_main_page(self):
        return self.find_element_and_value("weight_value", "main_page_element")

    def click_weight_layout(self):
        self.find_element_and_click("weight_layout", "main_page_element")

    def get_weight_mine_page(self):
        return self.find_element_and_value("weight", "weight_page_element")

    def get_steps_main_page(self):
        return self.find_element_and_value("steps_number", "main_page_element")

    def click_steps_layout(self):
        self.find_element_and_click("steps_layout", "main_page_element")

    def to_mine_sport_page(self):
        self.find_element_and_click("mine_sport_tab", "status_page_element")

    def get_steps_today(self):
        steps_nums = self.find_element_and_name("total_steps_num", "status_page_element")
        steps_temp = steps_nums.split(",")[0]
        steps = steps_temp[1:]
        return steps


    def to_work_page(self):
        self.find_element_and_click("work_tab", "main_page_element")
        self.find_element_and_click("map_start_btn", "sport_page_element")

        self.find_element_and_click("sport_map_icon", "sport_page_element")
        if self.find_element("running_btn_location", "sport_page_element") != None:
            self.find_element_and_click("btn_close_map", "sport_page_element")
            self.find_element_and_click("running_pause", "sport_page_element")
            self.find_element_and_long_press("running_stop", "sport_page_element")
            self.find_element_and_click("GPS_signal_start", "sport_page_element")
            return True
        else:
            return False

    def to_run_outdoor_page(self):
        self.find_element_and_click("run_tab", "main_page_element")
        self.find_element_and_click("running_outdoors", "sport_page_element")
        self.find_element_and_click("map_start_btn", "sport_page_element")

        self.find_element_and_click("sport_map_icon", "sport_page_element")
        if self.find_element("running_btn_location", "sport_page_element") != None:
            self.find_element_and_click("btn_close_map", "sport_page_element")
            self.find_element_and_click("running_pause", "sport_page_element")
            self.find_element_and_long_press("running_stop", "sport_page_element")
            self.find_element_and_click("GPS_signal_start", "sport_page_element")
            return True
        else:
            return False


    def to_run_indoor_page(self):
        # self.find_element_and_click("run_tab", "main_page_element")
        self.find_element_and_click("running_indoors", "sport_page_element")
        self.find_element_and_click("map_start_btn", "sport_page_element")

        if self.find_element("running_pause", "sport_page_element") != None:
            self.find_element_and_click("running_pause", "sport_page_element")
            self.find_element_and_long_press("running_stop", "sport_page_element")
            self.find_element_and_click("GPS_signal_start", "sport_page_element")
            return True
        else:
            return False



    def to_cycling_page(self):
        self.find_element_and_click("cycling_tab", "main_page_element")
        self.find_element_and_click("map_start_btn", "sport_page_element")

        self.find_element_and_click("sport_map_icon", "sport_page_element")
        if self.find_element("running_btn_location", "sport_page_element") != None:
            self.find_element_and_click("btn_close_map", "sport_page_element")
            self.find_element_and_click("running_pause", "sport_page_element")
            self.find_element_and_long_press("running_stop", "sport_page_element")
            self.find_element_and_click("GPS_signal_start", "sport_page_element")
            return True
        else:
            return False

    def to_status_page(self):
        self.find_element_and_click("status_tab", "main_page_element")

    def to_advertisement_page(self):
        self.find_element_and_click("ad_img", "sport_page_element")

    def get_ad_element(self):
        return self.find_element("ad_img", "sport_page_element")

    def get_back_btn(self):
        return self.find_element("back_btn", "sport_page_element")

    def click_back_btn(self):
        self.find_element_and_click("back_btn", "sport_page_element")

    def get_ad_back_btn(self):
        return self.find_element("back_btn", "back_element")

    def to_practice_long_card(self):
        self.find_element_and_click("practice_long_card", "sport_page_element")

    def to_practice_short_card_1(self):
        self.find_element_and_click("practice_short_card_1", "sport_page_element")

    def get_classic_back_btn(self):
        return self.find_element("classic_back_btn", "sport_page_element")

    def click_classic_back_btn(self):
        self.find_element_and_click("classic_back_btn", "sport_page_element")

    def to_practice_short_card_2(self):
        self.find_element_and_click("practice_short_card_2", "sport_page_element")

    def to_competition_activity_page(self):
        self.find_element_and_click("competition_activity_btn", "sport_page_element")

    def to_hot_topic_first_card(self):
        self.find_elements_and_click("hot_topic_first_card", "sport_page_element", 0)

    def get_nick_element(self):
        return self.find_element("competition_activity_nick_name", "sport_page_element")

    def get_hot_topic_nick_name(self):
        return self.find_element_and_value("competition_activity_nick_name", "sport_page_element")

    def get_topic_page_nick_name(self):
        return self.find_element_and_value("page_nick_name", "sport_page_element")

    def to_hot_topic_second_card(self):
        self.find_element_and_click("hot_topic_second_card", "sport_page_element")

    def get_second_nick_name(self):
        return self.find_element_and_value("hot_topic_second_card_name", "sport_page_element")

    def to_hot_topic_third_card(self):
        self.find_element_and_click("hot_topic_third_card", "sport_page_element")

    def get_third_nick_name(self):
        return self.find_element_and_value("hot_topic_third_card_name", "sport_page_element")

    def get_sport_icon(self):
        return self.find_element("sport_tab", "main_page_element")


