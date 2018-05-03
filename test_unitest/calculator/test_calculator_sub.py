# -*- coding: utf-8 -*-

import unittest
from test_unitest.calculator.calculator import Calculator


class TestSub(unittest.TestCase):

    def setUp(self):
        print "test sub start"

    def test_sub(self):
        j = Calculator(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Calculator(71, 46)
        self.assertEqual(j.sub(), 25)

    def tearDown(self):
        print "test sub end"


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    # 运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)