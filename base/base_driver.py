import os

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from page.main_page import MainPage
from utils.write_user_command import WriteUserCommand
import pytest


class BaseDriver:
    # driver: WebDriver = None
    @classmethod
    # def andriod_driver(self, i):
    def andriod_driver(cls):
        # write_file = WriteUserCommand()
        # deviceName = write_file.get_value('user_info_'+str(i), 'deviceName')
        # port = write_file.get_value('user_info_'+str(i), 'port')
        caps = {}
        caps["platformName"] = "android"
        # caps["deviceName"] = "10.1.14.146:5555"
        caps["deviceName"] = os.environ["deviceName"]
        # caps["deviceName"] = "T8KVCE7P595SZ9VK"
        # caps["deviceName"] = deviceName
        caps["appPackage"] = "com.xiaomi.hm.health"
        caps["appActivity"] = "activity.StartUpActivity"
        caps["autoGrantPermissions"] = True
        caps["showChromedriverLog"] = True
        caps["noReset"] = True
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True
        caps["automationName"] = "UiAutomator2"
        caps["newCommandTimeout"] = "600"
        # udid = os.getenv("UDID", None)
        # if udid != None:
        #     caps["udid"] = udid
        #     print("udid = %s" % udid)

        cls.driver = webdriver.Remote("http://10.1.18.128:4723/wd/hub",caps)
        cls.driver.implicitly_wait(10)
        return MainPage(cls.driver)

        # self.driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub",caps)
        # self.driver.implicitly_wait(10)
        # return MainPage(self.driver)




    # @classmethod
    # def quit(cls):
    #     cls.driver.quit()







if __name__ == '__main__':
    read_ini = BaseDriver()
    # write_file = WriteUserCommand()
    driver = read_ini.andriod_driver()
