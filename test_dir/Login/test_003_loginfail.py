# 2025/6/6 17:12
# -*- coding:UTF-8 -*-

import sys
from os.path import dirname, abspath
from time import sleep

from pubmethod import waits
from page.lg_page import LgPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestLoginFail:
    """登录"""

    def test_login_fail_case(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入错误账号，错误密码
        3、点击登录按钮
        检查点：
        * 检查页面是否提示“账号或密码不正确”。
        """
        page = LgPage(driver)
        page.open(base_url)

        # 显示等待提成了公共方法
        waits.waits(driver, "ID", "login_userName", "qianchuan1")
        # 显示等待
        # myelement = WebDriverWait(driver,5,0.5).until(
        #     EC.visibility_of_element_located((By.ID,"login_userName"))
        # )
        # myelement.send_keys('qianchuan')

        # 隐式等待
        # driver.implicitly_wait(10)

        # 因为显示等待和PO的冲突 第一个元素就不使用PO模式了
        # page.login_account = "qianchuan1"
        page.login_pwd = "Qianchuan@1234"
        page.login_code = "1111"
        page.login_login_button.click()

        sleep(0.5)
        assert page.login_error_message.text == "账号或密码不正确"

