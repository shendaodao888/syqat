from poium import Page, Element


class LgPage(Page):
    login_account = Element(id_="login_userName", describe="用户名")
    login_pwd = Element(id_="login_password", describe="密码")
    login_code = Element(css = "#login_validateCode > span > input", describe="验证码")
    login_login_button = Element(css = "#login > button", describe="登录按钮")
    login_error = Element(css="body > div.ant-message.ant-message-top.css-5wsri9 > div > div > div > div > span:nth-child(2)", describe="账号密码错误")
    logout_button = Element(css = "#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > div > div > div.header_container___PmbyR > div.right_part___C6yxn > span.flex.items-center > span", describe="退出按钮")


    # 系统管理
    sys_manage_menu = Element(css="#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > div > div > div.header_container___PmbyR > div.h_container___ilIj4 > ul > li:nth-child(5)",describe="系统管理菜单")
    user_manage_left = Element(css="#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > div > div > div.ant-layout.ant-layout-has-sider.css-n81ky1 > aside > div > ul > li.ant-menu-item.ant-menu-item-selected.menu_item____GwTS > span.ant-menu-title-content",describe="左侧用户管理菜单按钮")