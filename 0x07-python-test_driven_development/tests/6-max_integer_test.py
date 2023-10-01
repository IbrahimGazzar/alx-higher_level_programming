#!/usr/bin/python3
"""
    This module is a unittest module for the function
    max_integer in the module 6-max_integer.py
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        A unittest class to be used for testing
        the max_integer function
    """
    def setUp(self):
        """
            Sets up the lists that we will use to test
            our function on
        """
        self.list_1 = [0, -10, -98, 2, 2, -5]
        self.list_2 = [0, 0, 0, 0, -1, 0]
        self.list_3 = [10, 9, 5, 1]
        self.list_0 = []
        self.list_4 = [4]
        self.list_5 = [-1, -2, -3, -4, -5]

    def test_max(self):
        """
            This function contains various test cases
            for max_integer, using the lists defined in
            the setup function
        """
        self.assertEqual(max_integer(self.list_1), 2)
        self.assertEqual(max_integer(self.list_2), 0)
        self.assertEqual(max_integer(self.list_3), 10)
        self.assertEqual(max_integer(self.list_4), 4)
        self.assertEqual(max_integer(self.list_5), -1)
        self.assertEqual(max_integer(self.list_0), None)
        self.assertEqual(max_integer(), None)
