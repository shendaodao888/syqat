import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig

# 项目目录配置
from page.lg_page import LgPage
from pubmethod import waits

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"

# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def driver():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver
    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        chrome_options = CH_Options()
        driver = Remote(command_executor='http://localhost:4444/wd/hub', options=chrome_options)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    yield driver

    driver.quit()

    return driver


# 登录
# autouse默认就是false，这里还写出来，是为了强调下最好使用false
@pytest.fixture(scope="class", autouse=False)
def login_setup(driver, base_url):
    """登录操作， 供多个测试类复用"""
    page = LgPage(driver)
    page.open(base_url)
    # 显示等待提成了公共方法
    waits.waits(driver, "ID", "login_userName").send_keys("qianchuan")
    page.login_pwd = "Qianchuan@123"
    page.login_code = "1111"
    page.login_login_button.click()
    # 测试结束后可清理，为了避免每次都要登录，这里暂时注释掉
    yield
    # page.logout.click()


# 设置用例描述表头
# def pytest_html_results_table_header(cells):
#     cells.insert(3, '<th>Description</th>')
#     cells.pop()


# 设置用例描述表格
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, f'<td>{report.description}</td>')
#     cells.pop()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     """
#     用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = description_html(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             case_path = report.nodeid.replace("::", "_") + ".png"
#             if "[" in case_path:
#                 case_name = case_path.split("-")[0] + "].png"
#             else:
#                 case_name = case_path
#             capture_screenshots(case_name)
#             img_path = "image/" + case_name.split("/")[-1]
#             if img_path:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % img_path
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

# @pytest.hookimpl(hookwrapper=True)
# def description_html(desc):
#     """
#     将用例中的描述转成HTML对象
#     :param desc: 描述
#     :return:
#     """
#     if desc is None:
#         return "No case description"
#     desc_ = ""
#     for i in range(len(desc)):
#         if i == 0:
#             pass
#         elif desc[i] == '\n':
#             desc_ += ";"
#         else:
#             desc_ += desc[i]
#
#     desc_lines = desc_.split(";")
#
#     head = f"<head><meta name='Content-Type' content='text/html; charset=latin1'></head>"
#
#     # 构建 HTML 正文部分
#     body = "<body>"
#     for line in desc_lines:
#         body += f"<p>{line}</p>"
#     body += "</body>"
#
#     # 完整的 HTML 文档
#     desc_doc = f"<html>{head}{body}</html>"
#
#     return desc_doc


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)





if __name__ == "__main__":
    capture_screenshots("test_dir/test_lg.png")
