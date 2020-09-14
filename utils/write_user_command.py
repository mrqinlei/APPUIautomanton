#coding=utf-8


import yaml
from config.file_config import FileConfig

class WriteUserCommand:

    def read_data(self):
        """
        获取数据
        :return:
        """
        with open(FileConfig().get_path(), 'r') as fr:
            data = yaml.safe_load(fr)
        return data

    def get_value(self, key, value):
        """
        获得对应字段的值
        :param key:
        :param value:
        :return:
        """
        data = self.read_data()
        value = data[key][value]
        return value

    def write_data(self,  i, deviceName, bp, port):
        """
        写入数据
        :param data:
        :return:
        """
        data = self.join_data( i, deviceName, bp, port)
        with open(FileConfig().get_path(), 'a') as fr:
            yaml.dump(data, fr)

    def join_data(self, i, deviceName, bp, port):
        """
        插入数据
        :param i:
        :param deviceName:
        :param bp:
        :param port:
        :return:
        """
        data = {
            "user_info_" + str(i) : {
                "deviceName" : deviceName,
                "bp" : bp,
                "port" : port
            }
        }
        return data

    def clear_data(self):
        """
        清楚数据
        :return:
        """
        with open(FileConfig().get_path(), 'w') as fr:
            fr.truncate()
        fr.close()


if __name__ == "__main__":
    write = WriteUserCommand()
    # print(write.get_value("user_info_0", "bp"))
    print(write.read_data())
