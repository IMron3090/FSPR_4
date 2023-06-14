"""
python - unittest
python -m unittest -v

"""

import unittest

import random_num

class TestPlusFunction (unittest.TestCase):
    def test_plus (self):
        test_num = 10
        result = random_num.plus(test_num)
        self.assertEqual(result, 15)

    def test_plus_passing_string (self):
        test_num= 10
        result = random_num.plus(test_num)
        self.assertNotEqual (result, 10) # 15 - 10

    def test_plus_passing_string (self):
        test_val = "a"
        result = random_num.plus(test_val)
        self.assertIsInstance(result, TypeError)


unittest.main()