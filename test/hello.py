# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
#
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()

# browser.quit()
#
# try:
#     browser.get("http://123123")
# except BaseException as msg:
#     print "hello" + str(msg)

for i in browser.find_elements(By.TAG_NAME, "input"):
    print i.get_attribute("name")

