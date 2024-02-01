#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [2, 35]
        msg = "Both are not equal"
        result = summation(data)
        self.assertEqual(result,65, msg)

if __name__ == '__main__':
    unittest.main()
