# 2025/6/13 13:46
# -*- coding:UTF-8 -*-
from time import sleep
import allure
import pytest
from page.lg_page import LgPage


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    @allure.title('删除用户')
    @allure.description('删除单个用户')
    @pytest.mark.parametrize("keyword, expect_result", [
        ("自动化测试-改", "自动化测试-改")
    ])
    def test_sys(self,  driver, base_url, keyword, expect_result):
        page = LgPage(driver)

        # 进入系统管理模块
        page.sys_manage_menu.click()
        page.user_manage_search_name.clear()
        page.user_manage_search_name.send_keys(keyword)
        sleep(1)
        assert page.user_manage_searched_name.text == expect_result
        div1 = page.user_manage_user_div.get_element_object()

        driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth;", div1)

        # 获取一组元素，会返回一个list
        options = page.user_manage_update_options

        # 点击删除
        options[1].click()
        page.user_manage_update_confirm.click()

        assert page.user_manage_update_delete_message.text == "删除成功"




