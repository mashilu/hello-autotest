# -*- coding: utf-8 -*-
import unittest
import test_baidu
import test_youdao
from HTMLTestRunner import HTMLTestRunner
import time


suite = unittest.TestSuite()
suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_youdao.MyTest("test_youdao"))

# 按照一定格式获取当前时间
now = time.strftime("%Y-%m-%d %H_%M_%S")

# 定义报告存放路径
filename = './' + now + '_result.html'
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner(stream=fp,
                        title=u'百度搜索测试报告',
                        description=u'用例执行情况')
# runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()

