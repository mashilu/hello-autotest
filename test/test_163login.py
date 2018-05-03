# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.163.com")

login = driver.find_element_by_id("js_N_navHighlight")
ActionChains(driver).move_to_element(login).perform()
iframe_login = driver.find_element_by_xpath("//*[@id='js_N_login_wrap']/iframe[1]")
driver.switch_to.frame(iframe_login)

# 获取用户名，密码，登录控件
email = WebDriverWait(driver, 10, 1).until(
    expected_conditions.presence_of_all_elements_located((By.XPATH, "//input[@name='email']"))
)
password = WebDriverWait(driver, 10, 1).until(
    expected_conditions.presence_of_all_elements_located((By.XPATH, "//input[@name='password']"))
)
login_btn = WebDriverWait(driver, 10, 1).until(
    expected_conditions.presence_of_all_elements_located((By.ID, "dologin"))
)

# 输入登录数据，并登录
email[0].send_keys("*********")
password[0].send_keys("***********")
sleep(5)
login_btn[0].click()

driver.switch_to.default_content()
sleep(5)
# 鼠标悬停登录后的用户名处，获取弹出功能列表
user_name = driver.find_element_by_id("js_N_navUsername")
ActionChains(driver).move_to_element(user_name).perform()

# 定位/跳转我的邮箱

# 获取首页窗口句柄
index_handle = driver.current_window_handle
driver.implicitly_wait(5)
my_email = driver.find_element_by_xpath("//*[@id='js_logined_suggest']/li[2]/a/span")
my_email.click()

# 我的邮箱打开后获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 定位收件箱

# 跳转到我的邮箱窗口
for handle in all_handles:
    if handle != index_handle:
        driver.switch_to.window(handle)
        driver.implicitly_wait(3)
        recv_box = driver.find_element_by_xpath("//*[@id='dvNavTree']/ul[1]/li[1]/div/span[2]")
        recv_box.click()

