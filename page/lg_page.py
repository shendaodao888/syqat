from poium import Page, Element, Elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LgPage(Page):
    # 登录登出
    login_account = Element(id_="login_userName", describe="用户名")
    login_pwd = Element(id_="login_password", describe="密码")
    login_code = Element(css="#login_validateCode > span > input", describe="验证码")
    login_login_button = Element(css="#login > button", describe="登录按钮")
    login_error_message = Element(css="body > div.ant-message.ant-message-top.css-5wsri9 > div > div > div > div > "
                                      "span:nth-child(2)", describe="账号密码错误")
    login_null_account = Element(css="#login_userName_help > div", describe="请输入账号")
    login_null_pwd = Element(css="#login_password_help > div", describe="请输入密码")
    login_null_valcode = Element(css="#login_validateCode_help > div", describe="请输入验证码")
    logout_button = Element(css="#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > "
                                "div > div > div.header_container___PmbyR > div.right_part___C6yxn > "
                                "span.flex.items-center > span", describe="退出按钮")
    remember_pwd_icon = Element(css="#login > div.passwordAction___xKGt0 > label > span:nth-child(2) > span > span > "
                                    "svg > path", describe="记住密码的叹号图标")
    remember_pwd_tips = Element(class_name="ant-tooltip-inner", describe="鼠标悬浮在icon上的提示信息")
    remember_pwd_checkbox = Element(css="#login > div.passwordAction___xKGt0 > label > span.ant-checkbox.ant-wave-target.css-sr668d > input", describe="记住密码勾选框")
    logout = Element(css="#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > div > div > div.header_container___PmbyR > div.right_part___C6yxn > span.flex.items-center", describe="退出按钮")
    update_pwd = Element(css="#login > div.passwordAction___xKGt0 > span", describe="修改密码按钮")
    update_pwd_title = Element(class_name="hello___uuaxu", describe="修改密码页title")
    update_pwd_account = Element(id_="login_userAccount", describe="修改密码页的账号输入框")
    update_pwd_old_pwd = Element(id_="login_originPassword", describe="原密码")
    update_pwd_new_pwd = Element(id_="login_resetPassword", describe="新密码")
    update_pwd_confirm_pwd = Element(id_="login_confirmPassword", describe="确认密码")
    update_pwd_submit = Element(css="#login > button", describe="提交按钮")
    update_pwd_return = Element(class_name="text-base flex justify-center cursor-pointer hover:!text-red-700", describe="返回按钮")
    update_pwd_null_account = Element(css="#login_userAccount_help > div", describe="请输入账号")
    update_pwd_null_old_pwd = Element(css="#login_originPassword_help > div", describe = "请输入原密码")
    update_pwd_null_new_pwd = Element(css="#login_resetPassword_help > div", describe = "请输入新密码")
    update_pwd_null_confirm_pwd = Element(css="#login_confirmPassword_help > div", describe = "请确认新密码")
    update_pwd_old_pwd_error = Element(css="body > div.ant-message.ant-message-top.css-5wsri9 > div > div > div > div > span:nth-child(2)", describe="原密码不正确")
    update_new_confirm_pwd_inconsistency = Element(css="#login_confirmPassword_help > div", describe="新旧密码不一致")
    update_pwd_success = Element(css="#root > div.css-5wsri9.ant-app > div > div > div > div", describe="您的密码已修改成功！")
    Login_again = Element(css="#root > div.css-5wsri9.ant-app > div > div > div > button > span", describe="重新登录")


    # 系统管理
    sys_manage_menu = Element(css="#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > "
                                  "div > div > div.header_container___PmbyR > div.h_container___ilIj4 > ul > "
                                  "li:nth-child(5)", describe="系统管理菜单")
    user_manage_left = Element(css="#root > div.css-5wsri9.ant-app > div > div.ant-layout.css-5wsri9 > div > main > "
                                   "div > div > div.ant-layout.ant-layout-has-sider.css-n81ky1 > aside > div > ul > "
                                   "li.ant-menu-item.ant-menu-item-selected.menu_item____GwTS > "
                                   "span.ant-menu-title-content", describe="左侧用户管理菜单按钮")
    user_manage_buttons = Elements(xpath="//*[@id=\"scrollableDiv\"]/div/div[2]/div[2]/div[1]/div[1]/button", describe="一组操作按钮：新建用户、批量导入、导出、批量删除、批量禁用")
    user_manage_add_account = Element(id_="user_userAccount", describe="用户工号")
    user_manage_add_name = Element(id_="user_userName", describe="用户姓名")
    user_manage_add_phone = Element(id_="user_phoneNumber", describe="手机号")
    user_manage_add_department = Element(id_="user_departmentId", describe="归属组织")
    user_manage_add_department_select = Element(css="body > div:nth-child(4) > div > div > div > div > div.ant-select-tree-list > div > div > div > div:nth-child(1) > span.ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-open > span", describe="输入组织名称后显示的窗口")
    user_manage_add_pwd = Element(id_="user_password", describe="登录密码")
    user_manage_add_role = Element(id_="user_roleIds", describe="角色")
    user_manage_add_role_select = Element(css="body > div:nth-child(5) > div > div > div.rc-virtual-list > div > div > div > div > div", describe="角色选择框")
    user_manage_add_status = Element(css="#user_status > label:nth-child(1) > span.ant-radio.ant-wave-target > input", describe="用户状态")
    user_manage_add_save = Element(css="#user > div.ant-form-item.submitBtnBox___Du8zi.css-n81ky1 > div > div > div > div > button.ant-btn.css-n81ky1.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid > span", describe="保存")
    user_manage_add_cancel = Element(css="#user > div.ant-form-item.submitBtnBox___Du8zi.css-n81ky1 > div > div > div > div > button.ant-btn.css-n81ky1.ant-btn-default.ant-btn-color-default.ant-btn-variant-outlined.mr8___Q9BHE > span", describe="取消")
    user_manage_add_success_message = Element(css="body > div.ant-message.ant-message-top.css-5wsri9 > div > div > div > div > span:nth-child(2)", describe="新增成功")
    user_manage_search_name = Element(css="#scrollableDiv > div > div.content___wOMmp > div.homeBox___HdiWB > div.actionBox___ienmf > div.actionRight___GGPNw > span > input", describe="用户姓名搜索")
    user_manage_searched_name =Element(css="#scrollableDiv > div > div.content___wOMmp > div.homeBox___HdiWB > div.ant-table-wrapper.tableContainer___oW4hG.css-n81ky1 > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(2)", describe="搜索结果")
    user_manage_searched_nums = Element(css="#scrollableDiv > div > div.content___wOMmp > div.homeBox___HdiWB > div.ant-table-wrapper.tableContainer___oW4hG.css-n81ky1 > div > div > ul > li.ant-pagination-total-text", describe="搜索结果条数")
    user_manage_update_icon = Element(css="#scrollableDiv > div > div.content___wOMmp > div.homeBox___HdiWB > div.ant-table-wrapper.tableContainer___oW4hG.css-n81ky1 > div > div > div > div > div > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td:nth-child(11) > div > button:nth-child(1) > span:nth-child(2)", describe="修改按钮")
    user_manage_user_div = Element(css="#scrollableDiv > div > div.content___wOMmp > div.homeBox___HdiWB > div.ant-table-wrapper.tableContainer___oW4hG.css-n81ky1 > div > div > div > div > div", describe="用户数据div")
    user_manage_update_success = Element(css="body > div.ant-message.ant-message-top.css-5wsri9 > div > div > div > div > span:nth-child(2)", describe="修改成功")
    user_manage_update_options = Elements(css="#scrollableDiv > div > div.content___wOMmp > div.homeBox___HdiWB > div.ant-table-wrapper.tableContainer___oW4hG.css-n81ky1 > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(11) > div > button", describe="操作按钮：修改删除重置密码")
    user_manage_update_confirm = Element(css="body > div:nth-child(3) > div > div.ant-modal-wrap.ant-modal-centered > div > div:nth-child(1) > div > div.ant-modal-footer > button.ant-btn.css-n81ky1.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid > span", describe="确定按钮")
    user_manage_update_delete_message = Element(css="body > div.ant-message.ant-message-top.css-5wsri9 > div > div > div > div > span:nth-child(2)", describe="删除成功")



