from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class MinePage(BaseAction):
    # 我的- 登录/注册
    login_and_signup_button = By.XPATH, "//*[@text='登录/注册']"

    # 点击登录/注册
    @allure.step(title='我的 - 点击 登录/注册')
    def click_login_and_signup_button(self):
        self.click(self.login_and_signup_button)