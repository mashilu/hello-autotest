from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

driver.set_window_size(500, 600)

driver.find_element_by_id("kw").send_keys("selenium")

# 窗口大小修改后，控件重新加载？这里如果没有sleep，下面的语句会出现找不到控件的错误
sleep(2)
driver.find_element_by_id("su").click()

js = "window.scrollTo(100, 450)"
driver.execute_script(js)
sleep(3)

driver.quit()

