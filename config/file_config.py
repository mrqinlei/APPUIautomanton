#coding=utf-8

import os
import sys
import platform

class FileConfig:

    def __init__(self):
        # 获取电脑系统平台
        self.computer_sys = sys.platform
        # self.path = os.path.abspath(os.path.dirname(__file__)).split('MiFitAndroid')[0]
        self.path = os.path.abspath(os.path.dirname(__file__)).split('config')[0]
        # 项目路径
        # self.project_path = self.path + 'MiFitAndroid'
        self.project_path = self.path

    def get_path(self, type="report_path"):
        self.report_path = ""
        self.pics_path = ""
        self.logs_page = ""
        self.userconfig_path = ""
        self.element_path = ""
        self.apk_path =  ""

        if ("darwin" in self.computer_sys) or ("linux" in self.computer_sys):
            #mac or linux
            if type == "report":
                # 报告路径
                self.report_path = self.project_path + '/report'
                return self.report_path
            elif type == "pics":
                # 报告路径
                self.report_path = self.project_path + '/report'
                # 报告截图存放路径
                self.pics_path = self.report_path + '/pic/'
                return self.pics_path
            elif type == "logs":
                # 报告路径
                self.report_path = self.project_path + '/report'
                # 报告日志存放路径
                self.logs_page = self.report_path + '/logs/'
                return self.logs_page
            elif type == "element":
                # 元素定位文件路径
                self.element_path = self.project_path + "/config/element_center.ini"
                return self.element_path
            elif type == "apk":
                #覆盖安装用apk存放路径
                self.apk_path = self.project_path + "/apkstore/com.xiaomi.hm.health.apk"
                return self.apk_path
            else:
                # 填写设备信息路径
                self.userconfig_path = self.project_path + "/config/userconfig.yaml"
                return self.userconfig_path
        else:
            #windows
            if type == "report":
                # 报告路径
                self.report_path = self.project_path + '\\report'
                return self.report_path
            elif type == "pics":
                # 报告路径
                self.report_path = self.project_path + '\\report'
                # 报告截图存放路径
                self.pics_path = self.report_path + '\\pic\\'
                return self.pics_path
            elif type == "logs":
                # 报告路径
                self.report_path = self.project_path + '\\report'
                # 报告日志存放路径
                self.logs_page = self.report_path + '\\logs\\'
                return self.logs_page
            elif type == "element":
                #元素定位文件路径
                self.element_path = self.project_path + "\\config\\element_center.ini"
                return self.element_path
            else:
                # 填写设备信息路径
                self.userconfig_path = self.project_path + "\\config\\userconfig.yaml"
                return self.userconfig_path






if __name__ == "__main__":
    file = FileConfig()
    print(file.project_path)
    print(file.get_path(type="pics"))



