
from utils.dos_cmd import DosCmd


class Port:

    def port_is_used(self, port_num):
        """
        判断端口是否被占用
        :param port_num:
        :return:
        """
        flag = None
        self.dos = DosCmd()
        # result = self.dos.excute_cmd_result("netstat -ano | findstr" + port_num)#windows平台下的命令
        command = "lsof -i:" + str(port_num)
        result = self.dos.excute_cmd_result(command)#mac平台下的命令
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag


    def create_port_list(self, start_port, device_list):
        """
        生成可用的端口
        :param start_port: 开始端口号
        :param device_list: 设备列表
        :return:生成的对应设备的端口号
        """
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            print("生成可用端口失败")
            return None




if __name__ == "__main__":
    port = Port()
    # print (port.port_is_used(4723))
    li = [1,2,3,4,5]
    print(port.create_port_list(4723, li))
