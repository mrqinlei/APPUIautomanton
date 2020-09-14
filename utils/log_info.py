#coding=utf-8

import time
import os
import subprocess
from config.file_config import FileConfig
import allure
from utils.dos_cmd import DosCmd

class LogInfo:

    def __init__(self):
        self.dos_cmd = DosCmd()
        self.now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # self.filename = FileConfig().get_path(type="log") + self.now + r".txt"
        self.filename = self.now + r".txt"
        self.file_path = FileConfig().get_path(type="logs") + self.filename
        self.logcat_file = open(self.file_path, 'w')
        logcmd = "adb logcat -v time"
        self.Poplog = subprocess.Popen(logcmd, shell=True, stdout=self.logcat_file, stderr=subprocess.PIPE)
        # dos_cmd.excute_cmd(logcmd)


    def logEnd(self, log_doc):
        self.Poplog.terminate()
        file_object = open(self.file_path, 'rb')
        try:
            # for line in file_object:
            #     print(line)
            #     "\n"
            self.file = file_object.read()
        finally:
            allure.attach(self.file, log_doc, allure.attachment_type.TEXT)
            clear_logcat = "adb logcat -c"
            self.dos_cmd.excute_cmd(clear_logcat)
            file_object.close()
            self.logcat_file.close()



if __name__ == "__main__":
    log = LogInfo()
    log.logEnd("test")
