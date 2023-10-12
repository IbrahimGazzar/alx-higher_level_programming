#!/usr/bin/python3
"""
    Unittest folder for the class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
        Unittest class used for testing the
        base class
    """
    def setUp(self):
        """
            Set up function for all the needed tests
        """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(3)
        self.b4 = Base()
        self.b5 = Base(-9)
        self.b6 = Base(0)
        
    def test_base_id(self):
        """
            tests the values of base ids
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, -9)
        self.assertEqual(self.b6.id, 0)
