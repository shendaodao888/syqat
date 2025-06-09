# 2025/4/29 13:43
# -*- coding:UTF-8 -*-

import sys
from time import sleep

import allure
import pytest
from os.path import dirname, abspath

from selenium.webdriver.common.by import By

from page.lg_page import LgPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, dirname(dirname(abspath(__file__))))


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    """登录"""
    @allure.title('测试新增用户')
    @allure.description('测试正常新增用户')
    def test_sys(self, driver, base_url):
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
        page.sys_manage_menu.click()
        sleep(3)
        assert page.user_manage_left.text == "用户管理"

        




