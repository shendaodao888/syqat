# 2025/6/11 16:52
# -*- coding:UTF-8 -*-

from time import sleep
import allure
import pytest
from page.lg_page import LgPage


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    @allure.title('测试用户姓名搜索')
    @allure.description('测试用户姓名搜索')
    @pytest.mark.parametrize("keyword, expect_result", [
        ("自动化测试-改", "自动化测试-改"),
        ("qianchuan", "qianchuan")
    ])
    def test_sys(self, driver, base_url, keyword, expect_result):
        page = LgPage(driver)
        # 进入系统管理模块
        page.sys_manage_menu.click()
        page.user_manage_search_name.clear()
        page.user_manage_search_name.send_keys(keyword)
        sleep(1)
        assert page.user_manage_searched_name.text == expect_result
        sleep(1)

        # 当然这一条也可以参数化 但要保证测试数据匹配的起来
        assert page.user_manage_searched_nums.text == "共 1 条"

