import os

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.common.keys import Keys

from utils.read_init import ReadInit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
import allure
from config.file_config import FileConfig
import datetime
from utils.log_info import LogInfo
import subprocess


class BasePage:

    _black_list = [
        (By.ID, "升级框的元素定位"),
        (By.ID, "sport_ad_close"),
        (By.ID, "dialog_negative_button"),
        (By.ID, "advertisement_ball_cancel"),
        (By.ID, "dialog_positive_button"),
        (By.ID, "dialog_neutral_button"),
        (By.ID, "know_btn"),
        (By.ID, "permission_allow_button_1"),
        (By.ID, "know_btn")

    ]


    # def __init__(self, driver: WebDriver):
    def __init__(self, driver):
        self.driver = driver

    #查找元素
    def find_element(self, key, section=None, count=0):
        """
        查找对应单一元素
        :param key: 定位方式：id，name等
        :param section: 定位值
        :param count: 第几次查找
        :return: 定位到的元素
        """
        read_init = ReadInit()
        local = read_init.get_value(key, section)
        count = count

        if local is not None:
            by = local.split('>')[0]
            _local_by = local.split('>')[1]
            logging.info(u"正在 %s 页面通过 %s 查找 %s元素" % (self, by, _local_by))

            try:
                if by == "id":
                    return WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_id(_local_by))
                elif by == 'className':
                    return WebDriverWait(self.driver, 15).until(
                        EC.visibility_of_element_located(By.CLASS_NAME, _local_by))
                elif by == 'name':
                    return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(By.NAME, _local_by))
                elif by == 'uiautomator':
                    return WebDriverWait(self.driver, 15).until(
                        lambda driver: driver.find_element_by_android_uiautomator(
                            'new UiSelector().text("%s")' % _local_by))
                elif by == 'uiautomator_id':
                    return WebDriverWait(self.driver, 15).until(
                        lambda driver: driver.find_element_by_android_uiautomator(
                            'new UiSelector().resourceId("%s")' % _local_by))
                elif by == 'accessibility':
                    return WebDriverWait(self.driver, 15).until(
                        lambda driver: driver.find_element_by_accessibility_id(_local_by))
                elif by == 'tag':
                    return WebDriverWait(self.driver, 15).until(
                        lambda driver: driver.find_element_by_tag_name(_local_by))
                elif by == 'partial_link':
                    return WebDriverWait(self.driver, 15).until(
                        lambda driver: driver.find_element_by_partial_link_text(_local_by))
                else:
                    return WebDriverWait(self.driver, 15).until(
                        lambda driver: driver.find_element_by_xpath(_local_by))
            except:
                logging.info(u"%s 页面中未能找到 %s 元素" % (self, _local_by))
                if count < 1:
                    self.handle_exception()
                    time.sleep(3)
                    return self.find_element(key, section, 1)
                else:
                    return None
        else:
            logging.info(u"在配置文件中没有找到%s元素的相关定位信息" % local)
            return None


    #查找并点击元素
    def find_element_and_click(self, key, section=None):
        element = self.find_element(key, section)
        if element is not None:
            element.click()
        else:
            logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")

    #查找并输入元素
    def find_element_and_sendKeys(self, key, section=None, context=None, isClick=False):
        element = self.find_element(key, section)
        if element is not None:
            if isClick is False:
                if context is not None:
                    element.send_keys(context)
                else:
                    logging.info(u"输入的信息不能为空")
            else:
                # self.driver.press_keycode(66)
                self.driver.keyevent(Keys.ENTER)
        else:
            logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")

    # 调起搜狗输入法 使用确定按钮，然后切回appium输入法
    def input_enter_search(self):
        os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')  # 调出搜狗输入法
        time.sleep(2)
        # os.system("adb -d shell input keyevent 66")

        # self.driver.keyevent(66)
        time.sleep(2)
        os.system('adb shell ime set io.appium.settings/.AppiumIME')


    #查找并返回文案
    def find_element_and_value(self, key, section=None):
        element = self.find_element(key, section)
        if element is not None:
            return element.get_attribute("text")
        else:
            logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")

    #查找并返回文案
    def find_element_and_name(self, key, section=None, action="contentDescription"):
        element = self.find_element(key, section)
        if element is not None:
            return element.get_attribute(action)
        else:
            logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")


    #查找并长按滑动
    def find_element_and_long_press(self, key, section=None):
        element = self.find_element(key, section)
        TouchAction(self.driver).long_press(element, duration=3000).perform()

    # 滑动到某个元素找某个元素
    def find_element_to_element(self, to_element_id=None):
        to_element_id = to_element_id
        if to_element_id is not None:
            try:
                return WebDriverWait(self.driver, 30).until(
                    lambda driver: driver.find_element_by_android_uiautomator(
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("%s")' % to_element_id))
            except:
                logging.info(u"%s 页面中未能找到元素" % self)
                return None
        else:
            logging.info(u"没有找到元素的相关定位信息")
            return None


    #查找一组元素
    def find_elements(self, key, section=None):
        """
        查找一组元素
        :param key: 定位方式
        :param section:  定位值
        :return: 一组元素
        """
        read_init = ReadInit()
        local = read_init.get_value(key, section)

        if local is not None:
            by = local.split(">")[0]
            _local_by = local.split(">")[1]
            logging.info(u"正在 %s 页面通过 %s 查找 %s元素" % (self, by, _local_by))

            try:
                if by == 'id':
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_id(_local_by))
                elif by == 'className':
                    # return self.driver.find_element_by_class_name(_local_by)
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_class_name(_local_by))
                elif by == 'android_uiautomator':
                    # return self.driver.find_element_by_name(_local_by)
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_android_uiautomator("text(\"%s\")" % _local_by))
                elif by == 'uiautomator':
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_android_uiautomator(
                            'new UiSelector().text("%s")' % _local_by))
                elif by == 'tag':
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_tag_name(_local_by))
                elif by == 'partial_link':
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_partial_link_text(_local_by))
                else:
                    # return self.driver.find_element_by_xpath(_local_by)
                    return WebDriverWait(self.driver, 30).until(
                        lambda driver: driver.find_elements_by_xpath(_local_by))
            except:
                logging.info(u"%s 页面中未能找到 %s 元素" % (self, _local_by))
                return None

        else:
            logging.info(u"在配置文件中没有找到%s元素的相关定位信息" %local)
            return None

    def find_elements_and_value(self, key, section=None, index=0):
        elements = self.find_elements(key, section)
        if elements is not None:
            return elements[index].get_attribute("text")
        else:
            logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")


    def find_elements_and_click(self, key, section=None, index=0):
        elements = self.find_elements(key, section)
        time.sleep(1)
        if elements is not None:
            elements[index].click()
        else:
            logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")

    #查找toast
    def find_toast_by_desc(self, content):
        try:
            # return WebDriverWait(self.driver, 30).until(
            #     lambda driver: driver.find_element_by_xpath("//*[@class='android.widget.Toast']"))
            return WebDriverWait(self.driver, 30).until(
                lambda driver: self.driver.find_element_by_xpath("//*[contains(@text, '"+content+"')]").text)
        except:
            return None

    #切换context
    def switch_to_webview(self):
        logging.info('--------%s----------' %(self.driver.contexts))
        contexts = self.driver.contexts
        # logging.info('--------%s----------' % (contexts[1]))
        # self.driver.switch_to.context(contexts[1])

        # 在获取到的contexts list里面去挨个循环
        for context in contexts:
            # 判断循环中单个的context是否是webview，如果是就进行切换，并且跳出循环
            if 'WEBVIEW' in context:
                self.driver.switch_to.context(context)
                logging.info(u'--------current_context:%s----------' %(self.driver.current_context))
                break



    def _get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width,height

    def _swipe_left(self):
        x1 = self._get_size()[0] / 10 * 9
        y1 = self._get_size()[1] / 2
        x = self._get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)

    def _swipe_right(self):
        x = self._get_size()[0] / 10 * 9
        y1 = self._get_size()[1] / 2
        x1 = self._get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)

    def _swipe_up(self):
        x1 = self._get_size()[0] / 2
        y1 = self._get_size()[1] / 10 * 9
        y = self._get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y)

    def _swipe_down(self):
        x1 = self._get_size()[0] / 2
        y1 = self._get_size()[1] / 10
        y = self._get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def _swipe_up_middle(self):
        x1 = self._get_size()[0] / 2
        y1 = self._get_size()[1] / 10 * 5
        y = self._get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y)

    def _swipe_up_bottom_to_middle(self):
        x1 = self._get_size()[0] / 2
        y1 = self._get_size()[1] / 10 * 9
        y = self._get_size()[1] / 10 *5
        self.driver.swipe(x1, y1, x1, y)

    def _swipe_up_bottom_right_to_middle(self):
        x1 = self._get_size()[0] / 4 * 3
        y1 = self._get_size()[1] / 10 * 9
        y = self._get_size()[1] / 10 * 5
        self.driver.swipe(x1, y1, x1, y)

    #滑动屏幕
    def swipe_on(self, direction=None):
        if direction == 'up':
            self._swipe_up()
        elif direction == 'down':
            self._swipe_down()
        elif direction == 'left':
            self._swipe_left()
        elif direction == 'right':
            self._swipe_right()
        elif direction == 'up_middle':
            self._swipe_up_middle()
        elif direction == 'up_bottom_to_middle':
            self._swipe_up_bottom_to_middle()
        elif direction == 'up_bottom_right_to_middle':
            self._swipe_up_bottom_right_to_middle()
        else:
            pass

    #处理异常控件的逻辑
    def handle_exception(self):
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            page_source = self.driver.page_source
            if "升级关闭按钮ID" in page_source:
                self.find_element(*locator).click()
            elif "其他弹框按钮ID" in page_source:
                self.find_element(*locator).click()
            elif "sport_ad_close" in page_source:#运动首页广告关闭按钮
                self.find_element_and_click("ad_close_btn", "alert_element")
            elif "permission_allow_button_1" in page_source:#运动首页系统权限弹窗的确定按钮
                self.find_element(*locator).click()
            elif "dialog_positive_button" in page_source:
                self.find_element_and_click("agree_btn", "alert_element")
            elif "dialog_negative_button" in page_source:
                self.find_element_and_click("do_not_disturb", "alert_element")
                # self.driver.find_element(*locator).click()
            elif "dialog_neutral_button" in page_source:
                self.find_element_and_click("worm_prompt", "sport_page_element")
            elif "know_btn" in page_source:
                self.find_element_and_click("know_btn", "alert_element")
                # self.driver.find_element(*locator).click()
            else:
                return None
            # elements = self.driver.find_elements(*locator)
            # if len(elements) >= 1:
            #     elements[0].click()
            # else:
            #     logging.info("%s元素未找到" % locator)
        self.driver.implicitly_wait(6)

    #保存截图
    def save_screenshots(self, img_doc):
        file_name = FileConfig().get_path(type="pics") + "{}_{}.png".format(datetime.datetime.now().strftime("%Y-%m-%d %H%M%S"), img_doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        # return file_name
        allure.attach(file, img_doc, allure.attachment_type.PNG)
        # case_logger.info("页面截图文件保存在：{}".format(file_name))


    def press_back_phone(self, count=1):
        while count == 0:
            self.driver.keyevent(4)
            count -= 1

    """
    点击原生的返回按钮
    """
    def click_back_by_native(self, type='back', count=1):
        for i in range(count):
            if type == 'back':
                element = self.find_element("back_btn", "back_element")
            elif type == 'title':
                element = self.find_element("title_back_btn", "back_element")
            elif type == 'find':
                element = self.find_element("find_back_btn", "back_element")
            elif type == "friend":
                element = self.find_element("friend_back_btn", "back_element")
            elif type == "home_page":
                element = self.find_element("home_page_back_btn", "back_element")
            else:
                element = self.find_element("left_btn", "back_element")

            if element is not None:
                element.click()
            else:
                logging.info(u"没有找到这个元素或没有在配置文件中找到对应定位信息")
            i += 1



    def get_device_state_custom(self):

        print (self.driver.session_id)
        print (str(self.driver.current_package))
        print (self.driver.query_app_state("com.xiaomi.hm.health"))

    # def save_logs_info(self, log_doc):
    #     log_file = self.logInfo.logEnd()
    #     # logcat_file = open(log_file, 'rb')
    #     # try:
    #     #     file = logcat_file.read()
    #     # finally:
    #     #     pass
    #     allure.attach(log_file, log_doc, allure.attachment_type.TEXT)




