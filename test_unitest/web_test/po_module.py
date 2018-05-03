# -*- coding: utf-8 -*-

# test page object model
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'http://www.163.com'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    """
    163邮箱登录页面类型
    """
    url = '/'

    # 定位器
    # 鼠标移动至该控件后弹出登录frame
    log_loc = (By.ID, "js_N_navHighlight")
    # 登录frame
    login_frame_loc = (By.XPATH, "//*[@id='js_N_login_wrap']/iframe[1]")
    # 登录frame中email用户名
    email_loc = (By.XPATH, "//input[@name='email']")
    # 登录frame中登录密码
    password_loc = (By.XPATH, "//input[@name='password']")
    # 登录frame中登录按钮
    login_btn_loc = (By.ID, "dologin")

    # Action
    # 切换到登录iframe
    def switch_to_login_iframe(self):
        login = self.find_element(*self.log_loc)
        ActionChains(self.driver).move_to_element(login).perform()
        iframe_login = self.driver.find_element(*self.login_frame_loc)
        self.driver.switch_to.frame(iframe_login)

    def type_email(self, email_content):
        email_tbox = WebDriverWait(self.driver, 10, 1).until(
            expected_conditions.presence_of_all_elements_located(self.email_loc)
        )
        email_tbox[0].send_keys(email_content)

    def type_password(self, password_content):
        password_tbox = WebDriverWait(self.driver, 10, 1).until(
            expected_conditions.presence_of_all_elements_located(self.password_loc)
        )
        password_tbox[0].send_keys(password_content)

    def submit(self):
        login_btn = WebDriverWait(self.driver, 10, 1).until(
            expected_conditions.presence_of_all_elements_located(self.login_btn_loc)
        )
        login_btn[0].click()


def test_user_login(a_driver, a_email, a_password):
    """
    测试获取的用户名、密码是否可以登录
    :param a_driver:
    :param a_email:
    :param a_password:
    :return:
    """
    login_page = LoginPage(a_driver)
    login_page.open()
    login_page.switch_to_login_iframe()
    login_page.type_email(a_email)
    login_page.type_password(a_password)
    login_page.submit()


if __name__ == '__main__':
    try:
        driver = webdriver.Firefox()
        email = 'mslbuaa@163.com'
        password = 'msl327528%%'
        test_user_login(driver, email, password)
        sleep(3)
    finally:
        driver.close()

