# -*- coding: utf-8 -*-
from test_unitest.calculator.calculator import Calculator
import unittest


class TestAdd(unittest.TestCase):

    def setUp(self):
        print "test add start"

    def test_add(self):
        j = Calculator(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Calculator(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self):
        print "test add end"

