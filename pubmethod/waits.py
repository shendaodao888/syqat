# 2025/6/6 15:59
# -*- coding:UTF-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waits(driver,type,element,text):
    # 显示等待
    if type == 'ID':
        myelement = WebDriverWait(driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.ID, element))
        )
        # myelement.send_keys(text)
    elif type == 'CSS_SELECTOR':
        myelement = WebDriverWait(driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element))
        )
    myelement.send_keys(text)



