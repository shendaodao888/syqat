# 2025/6/6 17:15
# -*- coding:UTF-8 -*-

import sys, allure
from os.path import dirname, abspath
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pubmethod import waits
from page.lg_page import LgPage


@allure.suite('登录')
@allure.feature('记住密码')
class TestLoginFail:
    """登录"""

    @allure.title('测试登录时记住密码')
    @allure.description('测试勾选记住密码登录登出后密码仍未清除')
    def test_login_remember_pwd_case(self, driver, base_url):
        page = LgPage(driver)
        page.open(base_url)

        # get_element_object()是获取底层的WebElement,因为接下来的鼠标悬浮需要的参数类型必须是WebElement
        icon = page.remember_pwd_icon.get_element_object()
        print("这是po模式下获取到的元素属性：", type(icon))

        # icon2 = driver.find_element(By.CSS_SELECTOR,value="#login > div.passwordAction___xKGt0 > label >
        # span:nth-child(2) > span > span > " "svg > path") print(type(icon2), '这是非PO模式获取的方式')

        ActionChains(driver).move_to_element(icon).perform()
        assert page.remember_pwd_tips.text == "*选中后，一个月内无需重复输入账号和密码"

        page.remember_pwd_checkbox.click()
        sleep(0.5)
        assert page.remember_pwd_checkbox.is_selected()

        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName").send_keys("qianchuan")
        page.login_pwd = "Qianchuan@123"
        page.login_code = "1111"
        page.login_login_button.click()

        sleep(1)
        assert driver.title == "柳工大模型应用平台"

        # 点击退出按钮
        page.logout.click()
        sleep(1)

        # 校验记住了用户名和密码
        assert page.login_account.get_attribute('value') == "qianchuan"
        assert page.login_pwd.get_attribute('type') == "password"
        assert page.login_pwd.get_attribute('value') == "Qianchuan@123"

