# -*- coding: utf-8 -*-

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(u"自动化测试报告", 'utf-8')
    msg['From'] = 'mslbuaa@163.com'
    msg['To'] = '67162442@qq.com'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("mslbuaa@163.com", "msl327528")
    smtp.sendmail("mslbuaa@163.com", "67162442@qq.com", msg.as_string())
    smtp.quit()
    print "email has send out!"


# 查找测试报告目录中最新的测试报告文件
def find_new_report(test_report_dir):
    lists = os.listdir(test_report_dir)
    # print lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report_dir + "\\" + fn))
    file_new = os.path.join(test_report_dir, lists[-1])
    # print file_new
    return file_new


def run_test(dir_test, dir_report):
    discover = unittest.defaultTestLoader.discover(dir_test, pattern='test_*.py')
    now = time.strftime('%Y%m%d%H%M%S')
    file_name = dir_report + '\\' + now + '_result.html'
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(discover)
    fp.close()


if __name__ == "__main__":
    test_dir = '.'
    report_dir = '.\\result'
    run_test(test_dir, report_dir)
    new_report = find_new_report(report_dir)
    send_mail(new_report)

