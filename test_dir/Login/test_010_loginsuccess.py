# 2025/4/29 13:43
# -*- coding:UTF-8 -*-
import sys, allure
from time import sleep
import pytest
from os.path import dirname, abspath
from pubmethod import waits
from page.lg_page import LgPage
sys.path.insert(0, dirname(dirname(abspath(__file__))))


@allure.suite('登录')
@allure.feature('登录成功')
class TestLoginSuccess:
    """登录"""
    @allure.title('测试正确账号密码验证码的登录')
    @allure.description('登录成功：测试正确账号密码验证码登录')
    def test_login_success(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入正确账密
        3、点击登录按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = LgPage(driver)
        page.open(base_url)
        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName").send_keys("qianchuan")
        page.login_pwd = "Qianchuan@123"
        page.login_code = "1111"
        page.login_login_button.click()
        sleep(1)
        assert driver.title == "柳工大模型应用平台"