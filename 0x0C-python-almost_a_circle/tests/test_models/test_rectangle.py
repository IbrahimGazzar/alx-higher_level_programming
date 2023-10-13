#!/usr/bin/python3
"""
    This tests the rectangle class
"""
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
import io


class TestRectangle(unittest.TestCase):
    """
        Testing class used for the rectangle class
    """
    def setUp(self):
        """
            Set up function for testing
        """
        self.r1 = Rectangle(2, 5)
        self.r2 = Rectangle(9, 1, 3)
        self.r3 = Rectangle(3, 3, 1, 9, -1)

    def test_create_rect(self):
        """
            Tests rectangle attr validation
        """
        self.assertEqual(f"{self.r1.width}, {self.r1.height}, {self.r1.x},"
                         + f" {self.r1.y}, {self.r1.id}", "2, 5, 0, 0, 4")
        self.assertEqual(f"{self.r2.width}, {self.r2.height}, {self.r2.x},"
                         + f" {self.r2.y}, {self.r2.id}", "9, 1, 3, 0, 5")
        self.assertEqual(f"{self.r3.width}, {self.r3.height}, {self.r3.x},"
                         + f" {self.r3.y}, {self.r3.id}", "3, 3, 1, 9, -1")

    def test_rect_str(self):
        """
            Tests the string representation of rect
        """
        self.assertEqual(self.r1.__str__(), f"[Rectangle] ({self.r1.id}) "
                         + f"{self.r1.x}/{self.r1.y} - {self.r1.width}/"
                         + f"{self.r1.height}")
        self.assertEqual(self.r2.__str__(), f"[Rectangle] ({self.r2.id}) "
                         + f"{self.r2.x}/{self.r2.y} - {self.r2.width}/"
                         + f"{self.r2.height}")
        self.assertEqual(self.r3.__str__(), f"[Rectangle] ({self.r3.id}) "
                         + f"{self.r3.x}/{self.r3.y} - {self.r3.width}/"
                         + f"{self.r3.height}")

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

    def test_rect_area(self):
        """
            Tests the rectangle's area method
        """
        self.assertEqual(self.r1.area(), 10)
        self.assertEqual(self.r2.area(), 9)
        self.assertEqual(self.r3.area(), 9)

    def test_rect_display(self):
        """
            Tests the display function of rect
        """
        ex1 = "##\n##\n##\n##\n##\n"
        ex2 = "   #########\n"
        ex3 = "\n\n\n\n\n\n\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r1.display()
            ac1 = mock_stdout.getvalue()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            self.r2.display()
            ac2 = mock_stdout.getvalue()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            self.r3.display()
            ac3 = mock_stdout.getvalue()
        self.assertEqual(ac1, ex1)
        self.assertEqual(ac2, ex2)
        self.assertEqual(ac3, ex3)

    def test_rect_update(self):
        """
            Tests the update function of rect
        """
        self.r1.update(10, 10, 10, 10)
        self.assertEqual(self.r1.id, 10)
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r1.x, 10)
        self.r1.update(69)
        self.assertEqual(self.r1.id, 69)
        self.assertRaises(ValueError, self.r1.update, 10, -2)
        self.assertRaises(TypeError, self.r1.update, 10, "2")

        self.r1.update(x=4, y=1, id=0, height=4)
        self.assertEqual(self.r1.id, 0)
        self.assertEqual(self.r1.area(), 40)
        self.assertEqual(self.r1.x, 4)

        self.r1.update(10, id=9, width=3)
        self.assertEqual(self.r1.id, 10)
        self.assertEqual(self.r1.area(), 40)

    def test_rect_dict(self):
        """
            Tests the to_dict function of rect
        """
        dict_1 = {'id': self.r1.id, 'width': 2, 'height': 5, 'x': 0, 'y': 0}
        dict_2 = {'id': self.r2.id, 'width': 9, 'height': 1, 'x': 3, 'y': 0}
        dict_3 = {'id': -1, 'width': 3, 'height': 3, 'x': 1, 'y': 9}
        self.assertEqual(self.r1.to_dictionary(), dict_1)
        self.assertEqual(self.r2.to_dictionary(), dict_2)
        self.assertEqual(self.r3.to_dictionary(), dict_3)

    def TearDown(self):
        """
            Deletes objects after testing
        """
        del self.r1
        del self.r2
        del self.r3
