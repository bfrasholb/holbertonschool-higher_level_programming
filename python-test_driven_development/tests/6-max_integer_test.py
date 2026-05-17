#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with positive and negative integers"""
        self.assertEqual(max_integer([-10, 2, 5, -3]), 5)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_string_list(self):
        """Test with strings"""
        self.assertEqual(max_integer(["a", "z", "m"]), "z")


if __name__ == "__main__":
    unittest.main()
