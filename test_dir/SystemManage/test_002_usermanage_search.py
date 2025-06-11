# 2025/6/11 16:52
# -*- coding:UTF-8 -*-

from time import sleep
import allure
from page.lg_page import LgPage
from pubmethod import waits


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    """登录"""

    @allure.title('测试用户姓名搜索')
    @allure.description('测试用户姓名搜索')
    def test_sys(self, driver, base_url):
        page = LgPage(driver)

        # page.open(base_url)
        page.user_manage_search_name.send_keys("自动化测试")
        assert page.user_manage_searched_name.text == "自动化测试"
        sleep(1)
        assert page.user_manage_searched_nums.text == "共 1 条"

