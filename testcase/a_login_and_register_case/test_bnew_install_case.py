import time

from utils.dos_cmd import DosCmd
import allure
from utils.log_info import LogInfo
import pytest
import time
from config.file_config import FileConfig


"""
此模块用于初次安装小米运动apk，路径为根目录下小米运动apk包
若已经安装，则卸载后再安装
"""

@pytest.skip
@allure.feature("覆盖安装测试")
class Test_New_install:

    @classmethod
    def setup_class(cls):
        print("开始执行初次安装")
        cls.filepath = FileConfig().get_path(type="apk")
        cls.logInfo = LogInfo()
        # cls.path = ("../com.xiaomi.hm.health.apk")
        cls.check_command = "adb shell pm path com.xiaomi.hm.health"
        cls.install_command = "adb install " + cls.filepath
        cls.uninstall_command = "adb uninstall com.xiaomi.hm.health"

    @allure.story("初次安装测试")
    @allure.severity("block")
    def test_new_install(self):
        self.check_install = DosCmd.excute_cmd_result(self,command=self.check_command)

        if "package:/data/app/com.xiaomi.hm.health-7hJ0INef8qDHy10fkeKCCA==/base.apk" in self.check_install:
            self.uninstall = DosCmd.excute_cmd_result(self,command=self.uninstall_command)
            time.sleep(4)
            self.install = DosCmd.excute_cmd_result(self,command=self.install_command)
            # self.save_screenshots("初次安装截图")
            # self.logInfo.logEnd("初次安装日志")
            assert "Success" in self.install
        else:
            self.install = DosCmd.excute_cmd_result(self,command=self.install_command)
            assert "Success" in self.install


    def tear_down(self):
        pass
