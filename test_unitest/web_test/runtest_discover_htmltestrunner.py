# -*- coding: utf-8 -*-

import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import os

test_dir = ".\\"
result_dir = ".\\result"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == '__main__':

    now = time.strftime("%Y%m%d%H%M%S")
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    file_name = result_dir + "\\" + now + "_result.html"
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告',
                            description=u'用例执行情况：')

    runner.run(discover)
    fp.close()

