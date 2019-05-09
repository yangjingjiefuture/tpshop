from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self,driver):
        self.driver = driver

    # 查找一个元素
    def find_element(self,feature,timeout=10,poll=1):
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
    def find_elements(self, feature, timeout=10, poll=1):
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

