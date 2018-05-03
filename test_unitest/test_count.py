from count import is_prime
import unittest


class TestCount(unittest.TestCase):

    def setUp(self):
        print "test start"

    def test_case_1(self):
        self.assertTrue(is_prime(7))

    def test_case_2(self):
        self.assertFalse(is_prime(8))

    def tearDown(self):
        print("test end")


if __name__ == "__main__":
    unittest.main()

