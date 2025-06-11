# 2025/6/10 10:52
# -*- coding:UTF-8 -*-
import allure
from time import sleep
from pubmethod import waits
from page.lg_page import LgPage


@allure.suite('登录')
@allure.feature('修改密码失败')
class TestUpdatePWDFail:
    @allure.title('测试为空的情况下')
    @allure.description('测试账号、原密码、新密码、确认密码输入框都为空的情况下提交')
    def test_update_pwd_all_null(self, driver, base_url):
        page = LgPage(driver)
        page.open(base_url)

        # 校验跳转到修改密码页
        page.update_pwd.click()
        headline = waits.waits(driver, "class", "hello___uuaxu").text
        assert headline == "修改密码"

        # 直接点击提交按钮
        page.update_pwd_submit.click()
        # sleep(0.5)
        # 校验前端不能为空的提示信息
        assert page.update_pwd_null_account.text == "请输入账号"
        assert page.update_pwd_null_old_pwd.text == "请输入原密码"
        assert page.update_pwd_null_new_pwd.text == "请输入新密码"
        assert page.update_pwd_null_confirm_pwd.text == "请确认新密码"