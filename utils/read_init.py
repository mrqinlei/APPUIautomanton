import configparser
from config.file_config import FileConfig


class ReadInit:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = FileConfig().get_path(type="element")
        else:
            self.file_path = file_path

        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding='utf-8')
        return read_ini

    def get_value(self, key, section=None):
        if section == None:
            section = 'login_element'

        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value

# if __name__ == '__main__':
#    read_ini = ReadInit()
#    print(read_ini.get_value('go_login','login_element'))