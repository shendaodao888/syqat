# 2025/6/12 17:23
# -*- coding:UTF-8 -*-
# 2025/6/11 16:52
# -*- coding:UTF-8 -*-

from time import sleep
import allure
import pytest
from selenium.webdriver import Keys

from page.lg_page import LgPage


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    @allure.title('修改用户')
    @allure.description('测试修改用户信息')
    @pytest.mark.parametrize("keyword, expect_result", [
        ("自动化测试", "自动化测试")
    ])
    def test_sys(self, driver, base_url, keyword, expect_result):
        page = LgPage(driver)
        # 进入系统管理模块
        driver.refresh()
        page.sys_manage_menu.click()

        page.user_manage_search_name.send_keys(keyword)
        # sleep(1)
        div1 = page.user_manage_user_div.get_element_object()
        can_scroll = driver.execute_script("""
            return arguments[0].scrollWidth > arguments[0].clientWidth;
        """, div1)
        print(f"能否横向滚动: {can_scroll}")

        # 移到最右边
        driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth;", div1)

        # 点击修改按钮
        page.user_manage_update_icon.click()

        page.user_manage_add_name.clear()
        page.user_manage_add_name.send_keys(Keys.BACKSPACE*10)
        sleep(1)
        page.user_manage_add_name.send_keys("自动化测试-改")

        page.user_manage_add_save.click()
        sleep(0.5)

        assert page.user_manage_update_success.text == "修改成功"

        # 移回最左边
        driver.execute_script("arguments[0].scrollLeft = 0;", div1)

        assert page.user_manage_searched_name.text == "自动化测试-改"





