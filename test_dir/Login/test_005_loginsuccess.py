# 2025/4/29 13:43
# -*- coding:UTF-8 -*-
import os
import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from pubmethod import waits
from page.lg_page import LgPage
sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestLogin:
    """登录"""

    def test_login_success_case(self, driver, base_url):
        """
        名称：使用正确账密登录
        步骤：
        1、打开浏览器
        2、输入正确账密
        3、点击登录按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = LgPage(driver)
        page.open(base_url)
        # sleep(5)

        # 显示等待提成了公共方法
        waits.waits(driver,"ID", "login_userName", "qianchuan")
        #显示等待
        # myelement = WebDriverWait(driver,5,0.5).until(
        #     EC.visibility_of_element_located((By.ID,"login_userName"))
        # )
        # myelement.send_keys('qianchuan')

        #隐式等待
        # driver.implicitly_wait(10)

        # 因为显示等待和PO的冲突 第一个元素就不使用PO模式了
        # page.login_account = "qianchuan1"
        page.login_pwd = "Qianchuan@123"
        page.login_code = "1111"
        page.login_login_button.click()

        sleep(5)

        # 绝对路径
        current_file_path = os.path.abspath(__file__)

        # 获取项目根目录（假设 data 在项目根目录下）
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))

        image_path = os.path.join(project_root, "screenshot")

        driver.save_screenshot(image_path+ "\logingg.png")
        assert driver.title == "柳工大模型应用平台"
        # driver.quit()





#
# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "test_login1.py"])

