# 2025/6/16 15:12
# -*- coding:UTF-8 -*-

from time import sleep
import allure
from page.lg_page import LgPage


@allure.suite('系统管理')
@allure.feature('用户管理')
class TestSys:
    """登录"""

    @allure.title('测试组织名称查询')
    @allure.description('测试组织名称查询')
    def test_sys(self, login_setup,driver, base_url):
        page = LgPage(driver)

        # 进入系统管理模块
        page.sys_manage_menu.click()

        page.user_manage_org_search.send_keys("柳工集团")
        assert page.user_manage_org_search_result.text == "柳工集团"

        # 获取一组操作按钮
        page.user_manage_org_search_result.click()
        sleep(1)
        field = page.user_manage_org_search_user_result
        # for i in a:
        #     print(i.text, '==========')
        # 校验
        assert "勿删" in field[1].text

        assert field[3].text == "柳工集团"
        
        assert page.user_manage_org_search_user_result_nums.text == "共一条"
