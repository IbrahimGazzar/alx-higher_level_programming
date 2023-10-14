#!/usr/bin/python3
"""
    Unittest folder for the class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_base_json(self):
        """
            tests Base's to_json function
        """
        r1 = Rectangle(2, 2, 2, 2, 2)
        s1 = Square(10, 2, 3, 0)
        r1_dict = dict(sorted(r1.to_dictionary().items()))
        s1_dict = dict(sorted(s1.to_dictionary().items()))

        self.assertEqual(self.b1.to_json_string([r1_dict]), "[{\"height\": 2"
                         + ", \"id\": 2, \"width\": 2, \"x\": 2, \"y\": 2}]")
        self.assertEqual(self.b1.to_json_string([s1_dict]), "[{\"id\": 0, \""
                         + "size\": 10, \"x\": 2, \"y\": 3}]")
        self.assertEqual(self.b1.to_json_string([r1_dict, s1_dict]), "[{\""
                         + "height\": 2, \"id\": 2, \"width\": 2, \"x\": 2"
                         + ", \"y\": 2}, {\"id\": 0, \"size\": 10, "
                         + "\"x\": 2, \"y\": 3}]")

    def TearDown(self):
        """
            Deletes objects after testing
        """
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        del self.b6
