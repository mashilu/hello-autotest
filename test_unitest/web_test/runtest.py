# -*- coding: utf-8 -*-
import unittest
import test_baidu
import test_youdao

suite = unittest.TestSuite()
suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_youdao.MyTest("test_youdao"))

runner = unittest.TextTestRunner()
runner.run(suite)

