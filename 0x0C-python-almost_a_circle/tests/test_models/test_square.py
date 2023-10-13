#!/usr/bin/python3
"""
    This module contains the test suite for
    the Square Class and its methods
"""
import unittest
from unittest.mock import patch
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        Class used for testing the square class
    """
    def setUp(self):
        """
            Set up function for testing
        """
        self.s1 = Square(3)
        self.s2 = Square(2, 2)
        self.s3 = Square(4, 1, 4)
        self.s4 = Square(1, 2, 1, -1)

    def test_sqr_valid(self):
        """
            Tests the input validation of square
        """
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(TypeError, Square, 10, "zero", 9)
        self.assertRaises(ValueError, Square, -1, 2, 2)

    def test_sqr_str(self):
        """
            Tests the string representation of square
        """
        self.assertEqual(self.s1.__str__(), f"[Square] ({self.s1.id}) 0/0 - 3")
        self.assertEqual(self.s2.__str__(), f"[Square] ({self.s2.id}) 2/0 - 2")
        self.assertEqual(self.s3.__str__(), f"[Square] ({self.s3.id}) 1/4 - 4")
        self.assertEqual(self.s4.__str__(), "[Square] (-1) 2/1 - 1")

    def test_sqr_area(self):
        """
            Tests area calculation of square
        """
        self.assertEqual(self.s1.area(), 9)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 1)

    def test_sqr_display(self):
        """
            Tests the display function of square object
        """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.s1.display()
            ac1 = mock_stdout.getvalue()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            self.s2.display()
            ac2 = mock_stdout.getvalue()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            self.s3.display()
            ac3 = mock_stdout.getvalue()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            self.s4.display()
            ac4 = mock_stdout.getvalue()
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
        ex1 = "###\n###\n###\n"
        ex2 = "  ##\n  ##\n"
        ex3 = "\n\n\n\n ####\n ####\n ####\n ####\n"
        ex4 = "\n  #\n"
        self.assertEqual(ac1, ex1)
        self.assertEqual(ac2, ex2)
        self.assertEqual(ac3, ex3)
        self.assertEqual(ac4, ex4)

    def test_sqr_size(self):
        """
            Tests the size getter setter set of square
        """
        self.assertEqual(self.s1.size, 3)
        self.s1.size = 4
        self.assertEqual(self.s1.size, 4)
        self.assertEqual(self.s1.height, 4)
        with self.assertRaises(TypeError):
            self.s1.size = "9"
        with self.assertRaises(ValueError):
            self.s1.size = 0

    def test_sqr_update(self):
        """
            Tests the update function of square
        """
        self.s1.update(10, 10, 10, 10)
        self.assertEqual(self.s1.__str__(), "[Square] (10) 10/10 - 10")
        self.s1.update(4)
        self.assertEqual(self.s1.__str__(), "[Square] (4) 10/10 - 10")
        self.assertRaises(TypeError, self.s1.update, 3, "J", 0)
        self.assertRaises(ValueError, self.s1.update, 0, -1, "k", 10)

        self.s1.update(size=5, y=2, id=-6, x=1)
        self.assertEqual(self.s1.__str__(), "[Square] (-6) 1/2 - 5")
        self.assertRaises(ValueError, self.s1.update, id=1, x="2", size=-9)
        self.assertRaises(ValueError, self.s1.update, id=1, size=-9, x="2")

    def TearDown(self):
        """
            Deletes objects after testing
        """
        del self.s1
        del self.s2
        del self.s3
        del self.s4
