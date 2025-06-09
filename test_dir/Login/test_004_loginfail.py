# 2025/6/6 17:15
# -*- coding:UTF-8 -*-

import sys, allure
from os.path import dirname, abspath
from time import sleep

from pubmethod import waits
from page.lg_page import LgPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


@allure.suite('登录')
@allure.feature('登录失败')
class TestLoginFail:
    """登录"""
    @allure.title('测试空账号、空密码情况下的登录')
    @allure.description('登录失败：测试空账号、空密码登录')
    def test_login_fail_all_null_case(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入空账号，空密码
        3、点击登录按钮
        检查点：
        * 检查页面是否提示“请输入账号”、“请输入密码”、“请输入验证码”。
        """
        page = LgPage(driver)
        page.open(base_url)

        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName").send_keys("")
        page.login_pwd = ""
        page.login_code = ""
        page.login_login_button.click()

        sleep(0.5)
        assert page.login_null_account.text == "请输入账号"
        assert page.login_null_pwd.text == "请输入密码"
        assert page.login_null_valcode.text == "请输入验证码"

    @allure.title('测试空账号、其他正常输入的登录')
    @allure.description('登录失败：测试空账号、其他正常输入登录')
    def test_login_fail_account_null_case(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入空账号，其他正常输入
        3、点击登录按钮
        检查点：
        * 检查页面是否提示“请输入账号”、“请输入密码”、“请输入验证码”。
        """
        page = LgPage(driver)
        page.open(base_url)

        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName").send_keys("")
        page.login_pwd = "12345"
        page.login_code = "1111"
        page.login_login_button.click()

        sleep(0.5)
        assert page.login_null_account.text == "请输入账号"

    @allure.title('测试空密码、其他正常输入的登录')
    @allure.description('登录失败：测试空密码、其他正常输入登录')
    def test_login_fail_pwd_null_case(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入空密码，其他正常输入
        3、点击登录按钮
        检查点：
        * 检查页面是否提示“请输入账号”、“请输入密码”、“请输入验证码”。
        """
        page = LgPage(driver)
        page.open(base_url)

        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName").send_keys("qianchuan")
        page.login_pwd = ""
        page.login_code = "1111"
        page.login_login_button.click()

        sleep(0.5)
        assert page.login_null_pwd.text == "请输入密码"

    @allure.title('测试空验证码、其他正常输入的登录')
    @allure.description('登录失败：测试空验证码、其他正常输入登录')
    def test_login_fail_valcode_null_case(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入空验证码，其他正常输入
        3、点击登录按钮
        检查点：
        * 检查页面是否提示“请输入账号”、“请输入密码”、“请输入验证码”。
        """
        page = LgPage(driver)
        page.open(base_url)

        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName").send_keys("qianchuan")
        page.login_pwd = "12345"
        page.login_code = ""
        page.login_login_button.click()

        sleep(0.5)
        assert page.login_null_valcode.text == "请输入验证码"
