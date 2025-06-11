# 2025/6/10 15:04
# -*- coding:UTF-8 -*-

import allure
from time import sleep
from pubmethod import waits
from page.lg_page import LgPage


@allure.suite('登录')
@allure.feature('修改密码成功')
class TestUpdatePWDSuccess:
    @allure.title('测试修改密码成功的情况')
    @allure.description('测试修改密码成功的情况')
    def test_update_pwd_all_null(self, driver, base_url):
        page = LgPage(driver)
        page.open(base_url)

        # 校验跳转到修改密码页
        page.update_pwd.click()
        headline = waits.waits(driver, "class", "hello___uuaxu").text
        assert headline == "修改密码"

        # 输入正确的账号
        page.update_pwd_account.send_keys("autotest")
        # 输入正确原密码
        page.update_pwd_old_pwd.send_keys("12345@qaz")
        # 输入新密码并确认
        page.update_pwd_new_pwd.send_keys("123456@qaz")
        page.update_pwd_confirm_pwd.send_keys("123456@qaz")

        # 点击提交按钮
        page.update_pwd_submit.click()

        sleep(0.5)
        # 校验修改成功
        assert page.update_pwd_success.text == "您的密码已修改成功！"

        # 点击重新登录
        page.Login_again.click()

        # 使用新密码登录
        waits.waits(driver, "ID", "login_userName").send_keys("autotest")
        page.login_pwd = "123456@qaz"
        page.login_code = "1111"
        page.login_login_button.click()

        sleep(1)
        # 校验登录成功
        assert driver.title == "柳工大模型应用平台"

        # 点击退出按钮
        page.logout.click()

        # 恢复成初始密码
        # 校验跳转到修改密码页
        page.update_pwd.click()
        headline = waits.waits(driver, "class", "hello___uuaxu").text
        assert headline == "修改密码"

        # 输入正确的账号
        page.update_pwd_account.send_keys("autotest")
        # 输入正确原密码
        page.update_pwd_old_pwd.send_keys("123456@qaz")
        # 输入新密码并确认
        page.update_pwd_new_pwd.send_keys("12345@qaz")
        page.update_pwd_confirm_pwd.send_keys("12345@qaz")

        # 点击提交按钮
        page.update_pwd_submit.click()

        sleep(0.5)
        # 校验修改成功
        assert page.update_pwd_success.text == "您的密码已修改成功！"



