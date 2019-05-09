import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self,driver):
        self.driver = driver

    # 查找一个元素
    def find_element(self,feature,timeout=10.0,poll=1.0):
        """
        根据元素特征(元组)去定位一个元素方法
        :param feature: 特征
        :param timeout: 超时时间,默认10秒
        :param poll: 频率,默认1秒
        :return: 返回找到的元素
        """
        by,value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    # 查找一组元素
    def find_elements(self, feature, timeout=10.0, poll=1.0):
        """
        根据元素特征(元组)去定位一组元素方法
        :param feature: 特征
        :param timeout: 超时时间,默认10秒
        :param poll: 频率,默认1秒
        :return: 返回找到的元素
        """
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))


    # 点击元素
    def click(self, feature):
        self.find_element(feature).click()

    # 定位元素,输入内容
    def input(self, feature, content):
        self.clear(feature)
        self.find_element(feature).send_keys(content)

    # 定位元素,并清空
    def clear(self, feature):
        self.find_element(feature).clear()

    # 按返回键
    def press_back(self):
        self.driver.press_keycode(4)

    # 按回车键
    def press_enter(self):
        self.driver.press_keycode(66)

    # 屏幕截图
    def screen_shot(self, file_name):
        """
        屏幕截图,保存在image文件夹中
        :param file_name:  文件名
        :return: 是否截图成功
        """
        return self.driver.get_screenshot_as_file("./image/" + file_name)

    @staticmethod
    def allure_pic_with_local(title, file_name):
        """
        将本地的image中的某张图片,添加到allure报告中
        :param title:  allure标题
        :param file_name: image文件夹中的哪一个图片
        """
        with open("./image/" + file_name, "rb") as f:
            allure.attach(title, f.read(), allure.attach_type.PNG)

    # 获取toast文本内容
    def find_toast(self,message):
        toast_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        return self.find_element(toast_xpath, timeout=3, poll=0.1).text

    # 判断toast是否存在
    def is_toast_exits(self, message):
        try:
            self.find_element(message)
            return True
        except TimeoutException:
            return False


