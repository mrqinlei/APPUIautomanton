import os
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from page.main_page import MainPage
from utils.write_user_command import WriteUserCommand
import pytest
from utils.dos_cmd import DosCmd
from utils.port import Port


class BaseDriver:



    @classmethod
    def andriod_driver(cls):
        cmd_result = DosCmd()
        port_check = Port()
        # write_file = WriteUserCommand()
        # deviceName = write_file.get_value('user_info_'+str(i), 'deviceName')
        # port = write_file.get_value('user_info_'+str(i), 'port')
        #        Initialization = os.environ["Initialization"]
        caps = {}
        caps["platformName"] = "android"
        # caps["deviceName"] = "10.1.14.146:5555"
        #        caps["deviceName"] = os.environ["UDID"]
        caps["deviceName"] = "37KNW18614022787"
        # caps["deviceName"] = deviceName
        caps["appPackage"] = "com.xiaomi.hm.health"
        caps["appActivity"] = "activity.StartUpActivity"
        caps["autoGrantPermissions"] = True
        caps["showChromedriverLog"] = True
        caps["noReset"] = True
        Initialization = False
        if Initialization == True:
            caps["skipServerInstallation"] = False
            caps["skipDeviceInitialization"] = False
        else:
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True
        caps["automationName"] = "UiAutomator2"
        caps["newCommandTimeout"] = "600"
        if  caps["deviceName"] == "37KNW18614022787":

            cls.start_docker_server = cmd_result.excute_cmd_result("sudo docker run --privileged -d -p"+ " 4723"+":4723 --name"+" 37KNW18614022787" +" appium/appium")
            cls.driver = webdriver.Remote("http://10.1.18.116:"+"4723"+"/wd/hub",caps)
            cls.connect_appium_server = cmd_result.excute_cmd_result("sudo docker exec -i"+" 37KNW18614022787" +" adb connect"+" 37KNW18614022787" )
        else:
            cls.start_docker_server = cmd_result.excute_cmd_result("sudo docker run --privileged -d -p"+ " 4724"+":4723 --name"+" 4ad326fc" +" appium/appium")
            cls.driver = webdriver.Remote("http://10.1.18.116:"+"4724"+"/wd/hub",caps)
            cls.connect_appium_server = cmd_result.excute_cmd_result("sudo docker exec -i"+" 4ad326fc" +" adb connect"+" 4ad326fc" )
        # i = 4723
        # check_port = True
        # while check_port:
        #     cls.check_port = port_check.port_is_used(i)
        #     i=i+1
        #     port=i
        #     cls.start_docker_server = cmd_result.excute_cmd_result("sudo docker run --privileged -d -p"+ str(port)+":4723 --name"+"37KNW18614022787" +"appium/appium")
        # else:
        #     port=i
        #     cls.start_docker_server = cmd_result.excute_cmd_result("sudo docker run --privileged -d -p"+ str(port)+":4723 --name"+"37KNW18614022787" +"appium/appium")


        #self.start_docker_server = cmd_result.excute_cmd_result("sudo docker run --privileged -d -p"+ port+":4723 --name $UDID appium/appium")

        #cls.driver = webdriver.Remote("http://10.1.18.116:"+str(port)+"/wd/hub",caps)
        #cls.connect_appium_server = cmd_result.excute_cmd_result("sudo docker exec -i"+"37KNW18614022787" +"adb connect"+"37KNW18614022787" )        # cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        cls.driver.implicitly_wait(5)
        return MainPage(cls.driver)