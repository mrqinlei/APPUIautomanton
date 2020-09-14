import os
import subprocess



class DosCmd:

    def excute_cmd_result(self, command):
        """
        执行cmd命令并返回结果
        :param command:
        :return:
        """
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == "\n":
                continue
            result_list.append(i.strip("\n"))
        return result_list

    def excute_cmd(self, command):
        """
        执行cmd命令，无需返回结果
        :param command:
        :return:
        """
        # return os.system(command)
        # return subprocess.Popen(command, shell=True).stdout
        subprocess.call(command, shell=True)

if __name__ == "__main__":
    dos = DosCmd()
    print (dos.excute_cmd("adb devices"))
    # dos.excute_cmd()
