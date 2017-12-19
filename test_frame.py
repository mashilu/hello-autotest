# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import os
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath("frame.html")
print file_path

driver.get(file_path)

# 无法定位元素
try:
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
except NoSuchElementException as msg:
    print msg
finally:
    # 切换到iframe id='if'
    driver.switch_to.frame("if")

    # 正常操作定位元素
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()

    time.sleep(3)

    driver.quit()

