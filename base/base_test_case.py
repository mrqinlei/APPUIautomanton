import yaml
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseTestCase:


    def __init__(self, path):
        """
        读取yaml文件，对测试用例的操作步骤进行数据驱动
        :param path: 测试用例的路径
        """
        file = open(path, 'r')
        self.steps = yaml.safe_load(file)

    def run(self, driver):
        for step in self.steps:
            element = None
            if isinstance(step, dict):
                if "id" in step.keys():
                    element = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(step["id"]))
                elif "className" in step.keys():
                    element = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located(By.CLASS_NAME, step["className"]))
                elif "name" in step.keys():
                    element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(By.NAME, step["name"]))
                elif "uiautomator" in step.keys():
                    element = WebDriverWait(driver, 30).until(
                        lambda driver: driver.find_element_by_android_uiautomator(
                            'new UiSelector().text("%s")' % step["uiautomator"]))
                else:
                    element = WebDriverWait(driver, 30).until(
                        lambda driver: driver.find_element_by_xpath(step["xpath"]))



                if "input" in step.keys():
                    element.send_keys(step["input"])
                else:
                    element.click()

                if "get" in step.keys():
                    text = element.get_attribute(step["get"])
                    print (text)