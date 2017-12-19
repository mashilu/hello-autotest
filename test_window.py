# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 获得百度搜索窗口句柄
search_window = driver.current_window_handle

driver.find_element_by_link_text("登录").click()
driver.find_element_by_partial_link_text("注册").click()


# 获得当前所有打开窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != search_window:
        driver.switch_to.window(handle)
        print("===============注册窗口===============")
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys("mashilu")
        driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys("18888888888")
        time.sleep(2)

for handle in all_handles:
    if handle == search_window:
        driver.switch_to.window(handle)
        time.sleep(2)
        print("===============搜索窗口===============")
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        time.sleep(2)
        driver.find_element_by_id('kw').send_keys("selenium")
        driver.find_element_by_id('su').click()
        time.sleep(2)

driver.quit()


