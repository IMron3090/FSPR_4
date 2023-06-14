"""
python - unittest
python -m unittest -v

"""

import unittest

import Homework_29

class TestPlusFunction (unittest.TestCase):
    def test_plus (self):
        test_num = 10
        result = Homework_29.plus(test_num)
        self.assertEqual(result, 15)

    def test_plus_passing_string (self):
        test_num= 10
        result = Homework_29.plus(test_num)
        self.assertNotEqual (result, 10) # 15 - 10

    def test_plus_passing_string (self):
        test_val = "a"
        result = Homework_29.plus(test_val)
        self.assertIsInstance(result, TypeError)


unittest.main()