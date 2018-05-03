# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获取cookie信息
cookies = driver.get_cookies()
for cookie in cookies:
    print "%s ---- %s" % (cookie["name"], cookie["value"])

print "==========================================="

driver.add_cookie({'name': 'key-aaaaaa', 'value': 'value-bbbbbb'})
cookies = driver.get_cookies()
for cookie in cookies:
    print "%s ---- %s" % (cookie["name"], cookie["value"])

print "==========================================="
print cookies

driver.quit()

