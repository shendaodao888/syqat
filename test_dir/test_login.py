# 2025/4/29 13:43
# -*- coding:UTF-8 -*-

import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from page.lg_page import LgPage
sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestLogin:
    """登录"""

    def test_login_success_case(self, browser, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入正确账密
        3、点击登录按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = LgPage(browser)
        page.open(base_url)
        sleep(5)
        page.login_account = "qianchuan"
        page.login_pwd = "Qianchuan@123"
        page.login_code = "1111"
        page.login_login_button.click()
        sleep(5)

        assert browser.title == "柳工大模型应用平台"



#
if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])

