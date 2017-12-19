# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath("checkbox.html")
driver.get(file_path)

# 通过XPATH找到type=checkbox的元素
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

# 通过CSS找到type=checkbox元素
# checkboxes = driver.find_elements_by_css_selector("input[type=checkbox]")

for checkbox in checkboxes:
    checkbox.click()
    time.sleep(2)

# 打印当前页面上checkbox的个数
print len(checkboxes)

# 将最后一个checkbox的勾选去掉
checkboxes.pop().click()
time.sleep(2)

driver.quit()

