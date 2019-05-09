from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class LoginPage(BaseAction):
    # 用户名
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    # 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    # 登录按钮
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    # 输入用户名
    @allure.step(title='登录 - 输入 手机号')
    def input_username(self, content):
        allure.attach("输入手机号", content)
        self.input(self.username_edit_text,content)
    # 输入密码
    @allure.step(title='登录 - 输入 密码')
    def input_password(self, content):
        allure.attach("输入密码", content)
        self.input(self.password_edit_text, content)

    # 点击登录按钮
    @allure.step(title='登录 - 点击登录')
    def click_login_button(self):
        self.click(self.login_button)


    def is_login_button_enabled(self):
        """
        判断 登录按钮 是否可用
        :return:
            可用：true
            不可用：false
        """
        return not self.find_element(self.login_button).get_attribute("enabled") == "false"

        # if self.find_element(self.login_button).get_attribute("enabled") == "false":
        #     return not self.find_element(self.login_button).get_attribute("enabled") == "false"
        # else:
        #     return not self.find_element(self.login_button).get_attribute("enabled") == "false"


        # if self.find_element(self.login_button).get_attribute("enabled") == "false":
        #     return False
        # else:
        #     return True
