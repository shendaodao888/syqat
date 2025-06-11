# 2025/4/29 13:43
# -*- coding:UTF-8 -*-

import sys
from time import sleep
import allure
from os.path import dirname, abspath
from page.lg_page import LgPage

from pubmethod import waits


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    """登录"""
    @allure.title('测试新增用户')
    @allure.description('测试正常新增用户')
    def test_sys(self, driver, base_url):
        page = LgPage(driver)

        page.open(base_url)
        waits.waits(driver, "ID", "login_userName").send_keys("qianchuan")
        page.login_pwd = "Qianchuan@123"
        page.login_code = "1111"
        page.login_login_button.click()
        page.sys_manage_menu.click()
        assert page.user_manage_left.text == "用户管理"

        # 获取一组操作按钮
        buttons = page.user_manage_buttons
        # 操作新建用户
        buttons[0].click()
        sleep(0.5)

        page.user_manage_add_account.send_keys("at001")
        page.user_manage_add_name.send_keys("自动化测试")
        page.user_manage_add_phone.send_keys("18899998888")
        page.user_manage_add_department.send_keys()



        




