# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()

# 访问百度首页
index_url = "https://www.baidu.com"
print "now access first url %s" % index_url
driver.get(index_url)

# 访问新闻页面
news_url = "https://news.baidu.com"
print "now access second url %s" % news_url
driver.get(news_url)

# 返回到百度首页
print "back to %s" % index_url
driver.back()

# 前进到百度新闻页面
print "forward to %s" % news_url
driver.forward()

driver.quit()
