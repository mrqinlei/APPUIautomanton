from utils.dos_cmd import DosCmd
import allure
from utils.log_info import LogInfo
import pytest
from config.file_config import FileConfig


"""
此模块用于覆盖安装小米运动apk，路径为根目录下小米运动apk包
"""


@allure.feature("覆盖安装测试")
class Test_Recover_Install:

    @classmethod
    def setup_class(cls):
        print("开始执行覆盖安装")
        cls.filepath = FileConfig().get_path(type="apk")
        cls.logInfo = LogInfo()
        cls.command = "adb install -r " + cls.filepath

    @allure.story("覆盖安装测试")
    @allure.severity("block")
    def test_recover_install(self):
        self.install = DosCmd().excute_cmd_result(command=self.command)
        # self.save_screenshots("覆盖安装截图")
        # self.logInfo.logEnd("覆盖安装日志")
        assert "Success" in self.install

    def tear_down(self):
        pass
