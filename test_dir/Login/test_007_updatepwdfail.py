# 2025/6/10 10:52
# -*- coding:UTF-8 -*-
import allure
from time import sleep
from pubmethod import waits
from page.lg_page import LgPage


@allure.suite('登录')
@allure.feature('修改密码失败')
class TestUpdatePWDFail:
    @allure.title('测试原密码不正确的情况')
    @allure.description('测试原密码不正确的情况')
    def test_old_pwd_error(self, driver, base_url):
        page = LgPage(driver)
        page.open(base_url)

        # 校验跳转到修改密码页
        page.update_pwd.click()
        headline = waits.waits(driver, "class", "hello___uuaxu").text
        assert headline == "修改密码"

        page.update_pwd_account.send_keys("autotest")
        # 输入错误原密码
        page.update_pwd_old_pwd.send_keys("12345")
        #输入新密码并确认
        page.update_pwd_new_pwd.send_keys("123456@qaz")
        page.update_pwd_confirm_pwd.send_keys("123456@qaz")

        # 点击提交按钮
        page.update_pwd_submit.click()

        # 校验旧密码不正确
        assert page.update_pwd_old_pwd_error.text == "原始密码不正确"

    @allure.title('测试新密码和确认密码不一致的情况')
    @allure.description('测试新旧密码不一致的情况')
    def test_new_confirm_pwd_inconsistency(self, driver, base_url):
        page = LgPage(driver)
        page.open(base_url)

        # 校验跳转到修改密码页
        page.update_pwd.click()
        headline = waits.waits(driver, "class", "hello___uuaxu").text
        assert headline == "修改密码"

        page.update_pwd_account.send_keys("autotest")
        # 输入原密码
        page.update_pwd_old_pwd.send_keys("12345@qaz")
        # 输入新密码并确认
        page.update_pwd_new_pwd.send_keys("123456@qaz")
        page.update_pwd_confirm_pwd.send_keys("1234567@qaz")

        # 点击提交按钮
        page.update_pwd_submit.click()

        # 校验新旧密码不一致的提示信息
        assert page.update_new_confirm_pwd_inconsistency.text == "新旧密码不一致"