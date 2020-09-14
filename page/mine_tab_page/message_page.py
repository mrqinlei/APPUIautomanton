from base.base_page import BasePage


class MessagePage(BasePage):

    def get_message_counts(self):
        return self.find_element_and_value("red_dot", "mine_page_element")

    def get_message_icon(self):
        return self.find_element("message_icon", "mine_page_element")

    def to_message_page(self):
        return self.find_element_and_click("message_icon", "mine_page_element")

    def to_notif_tab(self):
        self.find_element_and_click("notification_counts", "mine_page_element")

    def to_select_notification_page(self):
        self.find_element_and_click("notification_select", "mine_page_element")

    def judge_h5_webview(self):
        return self.find_element("h5_flag","mine_page_element")

    def get_h5_webview_element_name(self):
        return self.find_element_and_value("h5_flag","mine_page_element")

    def get_notification_detail(self):
        return self.find_element_and_value("notification_detail", "mine_page_element")

    def get_fail_toast(self):
        return self.find_toast_by_desc(content="无网络，请检查网络")

    def to_message_tab(self):
        self.find_element_and_click("message_counts", "mine_page_element")

    def get_message_like_counts(self):
        return self.find_element_and_value("red_dot_like_counts", "mine_page_element")

    def get_message_comment_counts(self):
        return self.find_element_and_value("red_dot_comment_counts", "mine_page_element")

    def to_like_and_focus_page(self):
        self.find_element_and_click("message_counts", "mine_page_element")

    def to_like_page(self):
        self.find_element_and_click("like_layout", "mine_page_element")

    def to_comment_page(self):
        self.find_element_and_click("comment_layout", "mine_page_element")

    def to_follower_page(self):
        self.find_element_and_click("follow", "mine_page_element")

    def to_like_me_page(self):
        self.find_element_and_click("like", "mine_page_element")

    def find_follower_element(self):
        return self.find_element_and_value("follow_link_page_element", "mine_page_element")
