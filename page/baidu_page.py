from poium import Page, Element


class LgPage(Page):
    login_account = Element(id_="login_userName", describe="用户名")
    login_pwd = Element(id_="login_password", describe="密码")
    login_code = Element(css = "#login_validateCode > span > input", describe="验证码")
    login_login_button = Element(css = "#login > button", describe="登录按钮")