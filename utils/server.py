#coding=utf-8

import threading

from utils.dos_cmd import DosCmd
from utils.port import Port
from utils.write_user_command import WriteUserCommand
import time
from base.base_driver import BaseDriver


class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()
        self.base_driver = BaseDriver()

    def get_devices(self):
        """
        获得设备信息
        :return: 设备list
        """
        devices_list = []
        result_list = self.dos.excute_cmd_result("adb devices")

        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == "device":
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        """
        创建可用端口
        :param start_port:
        :return:
        """
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list


    def create_command(self, i):
        """
        根据设备个数，生成最终启动appium的命令行list
        :return:
        """
        # appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        command_list = []
        port_list = self.create_port_list(4700)
        bp_list = self.create_port_list(4900)
        device_list = self.device_list

        command = "appium -p " + str(port_list[i]) + " -bp " + str(bp_list[i]) + " -U " + device_list[i] + " --no-reset --session-override"
        command_list.append(command)
        self.write_file.write_data(i, device_list[i], str(bp_list[i]), str(port_list[i]))
        return command_list


    def start_server(self, i):
        """
        启动服务
        :param i:控制执行启动服务的次数，如果只有一个设备，则只启动一次服务，以此类推
        :return:
        """
        self.command_list = self.create_command(i)
        self.dos.excute_cmd(self.command_list[0])

    def kill_server(self):
        """
        杀掉appium进程
        :return:
        """
        server_list = self.dos.excute_cmd_result("ps aux |  grep appium")
        if len(server_list) > 0:
            self.dos.excute_cmd("pkill -f appium")

    def main(self):
        """
        多线程启动appium服务
        :return:
        """
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()
            time.sleep(10)



if __name__ == "__main__":
    server = Server()
    # print (server.device_list())
    # print(server.create_command())
    print(server.main())