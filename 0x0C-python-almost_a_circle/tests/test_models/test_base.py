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
        self.r1 = Rectangle(2, 2, 2, 2, 2)
        self.s1 = Square(10, 2, 3, 0)
        self.s2 = Square(4, 4, 4, 4)

    def test_base_0_id(self):
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
        r1_dict = dict(sorted(self.r1.to_dictionary().items()))
        s1_dict = dict(sorted(self.s1.to_dictionary().items()))

        self.assertEqual(self.b1.to_json_string([r1_dict]), "[{\"height\": 2"
                         + ", \"id\": 2, \"width\": 2, \"x\": 2, \"y\": 2}]")
        self.assertEqual(self.b1.to_json_string([s1_dict]), "[{\"id\": 0, \""
                         + "size\": 10, \"x\": 2, \"y\": 3}]")
        self.assertEqual(self.b1.to_json_string([r1_dict, s1_dict]), "[{\""
                         + "height\": 2, \"id\": 2, \"width\": 2, \"x\": 2"
                         + ", \"y\": 2}, {\"id\": 0, \"size\": 10, "
                         + "\"x\": 2, \"y\": 3}]")
        self.assertEqual(self.b1.to_json_string([]), "[]")

    def test_base_jfile(self):
        """
            Tests Base's JSON to file function
        """
        Rectangle.save_to_file([self.r1])
        Square.save_to_file([self.s1, self.s2])
        Base.save_to_file([])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[{\"height\": 2, \"id\": 2, "
                             + "\"width\": 2, \"x\": 2, \"y\": 2}]")
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[{\"id\": 0, \"size\": 10, "
                             + "\"x\": 2, \"y\": 3}, {\"id\": 4, "
                             + "\"size\": 4, \"x\": 4, \"y\": 4}]")
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_base_from_json(self):
        """
            Tests Base's from json function
        """
        r_dict = [self.r1.to_dictionary()]
        s_dict = [self.s1.to_dictionary(), self.s2.to_dictionary()]
        str1 = self.b1.to_json_string(r_dict)
        str2 = self.b1.to_json_string(s_dict)

        self.assertEqual(r_dict, self.b1.from_json_string(str1))
        self.assertEqual(s_dict, self.b1.from_json_string(str2))

    def test_base_create(self):
        """
            Tests Base's create function
        """
        s1_dup = Square.create(**(self.s1.to_dictionary()))
        r1_dup = Rectangle.create(**(self.r1.to_dictionary()))
        s3 = Square.create(**{'size': 5, 'id': 11})

        self.assertEqual(self.s1.__str__(), s1_dup.__str__())
        self.assertEqual(self.r1.__str__(), r1_dup.__str__())
        self.assertEqual(s3.__str__(), "[Square] (11) 0/0 - 5")

    def test_base_inst(self):
        """
            Tests the load from file function of Base
        """
        r_list = [self.r1]
        s_list = [self.s1, self.s2]
        b_list = []
        Base.save_to_file(b_list)
        Rectangle.save_to_file(r_list)
        Square.save_to_file(s_list)
        list_r = Rectangle.load_from_file()
        list_b = Base.load_from_file()
        list_s = Square.load_from_file()

        for i in range(len(list_r)):
            self.assertEqual(r_list[i].__str__(), list_r[i].__str__())
        for i in range(len(list_s)):
            self.assertEqual(s_list[i].__str__(), list_s[i].__str__())
        for i in range(len(list_b)):
            self.assertEqual(b_list[i].__str__(), list_b[i].__str__())

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
        del self.r1
        del self.s1
