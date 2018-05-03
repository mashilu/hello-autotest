from selenium import webdriver
from time import sleep
from time import ctime

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

print(ctime())
sleep(2)
print(ctime())

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

sleep(3)
print(ctime())

driver.quit()

