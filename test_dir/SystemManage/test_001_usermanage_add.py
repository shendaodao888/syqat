# 2025/4/29 13:43
# -*- coding:UTF-8 -*-

from time import sleep
import allure
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

        # page.open(base_url)
        driver.refresh()
        # 进入系统管理模块
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
        page.user_manage_add_department.send_keys("柳工集团")
        page.user_manage_add_department_select.click()
        page.user_manage_add_pwd.send_keys("12345@qaz")
        page.user_manage_add_role.send_keys("成员角色")
        page.user_manage_add_role_select.click()
        assert page.user_manage_add_status.is_selected()

        page.user_manage_add_save.click()
        sleep(0.5)
        assert page.user_manage_add_success_message.text == "新增成功"




        




