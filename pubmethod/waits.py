# 2025/6/6 15:59
# -*- coding:UTF-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waits(driver, type, element):
    myelement = None
    # 显示等待
    if type == 'ID':
        myelement = WebDriverWait(driver, 10, 0.5).until(
            EC.visibility_of_element_located((By.ID, element))
        )
    elif type == 'css':
        myelement = WebDriverWait(driver, 10, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element))
        )
    elif type == 'class':
        myelement = WebDriverWait(driver, 10, 0.5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, element))
        )
    elif type == 'xpath':
        myelement = WebDriverWait(driver, 10, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, element))
        )

    return myelement



