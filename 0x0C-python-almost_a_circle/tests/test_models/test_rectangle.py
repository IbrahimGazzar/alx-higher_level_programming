#!/usr/bin/python3
"""
    This tests the rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Testing class used for the rectangle class
    """
    def setUp(self):
        """
            Set up function for testing
        """
        self.r1 = Rectangle(10, 5)
        self.r2 = Rectangle(9, 8, 3)
        self.r3 = Rectangle(3, 10, 1, 9, -1)

    def test_create_rect(self):
        """
            Tests rectangle attr validation
        """
        self.assertEqual(f"{self.r1.width}, {self.r1.height}, {self.r1.x}, {self.r1.y}, {self.r1.id}", \
                         "10, 5, 0, 0, 4")
        self.assertEqual(f"{self.r2.width}, {self.r2.height}, {self.r2.x}, {self.r2.y}, {self.r2.id}", \
                         "9, 8, 3, 0, 5")
        self.assertEqual(f"{self.r3.width}, {self.r3.height}, {self.r3.x}, {self.r3.y}, {self.r3.id}", \
                         "3, 10, 1, 9, -1")

    def test_rect_valid(self):
        """
            Tests the validity of rectangle attrs
        """
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 2)
        self.assertRaises(TypeError, Rectangle, x=10, y=10)
        self.assertRaises(TypeError, Rectangle, "Hello", "World")
        self.assertRaises(TypeError, Rectangle, 9, 10, "!")
        self.assertRaises(ValueError, Rectangle, -1, 20)
        self.assertRaises(ValueError, Rectangle, 20, -1)
        self.assertRaises(ValueError, Rectangle, -1, "W")
        self.assertRaises(ValueError, Rectangle, 20, 10, 90, -1)
        
