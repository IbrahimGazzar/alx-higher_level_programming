#!/usr/bin/python3
"""
    This module contains the class Student
"""


class Student:
    """
        Simple class representing student information

        Attributes:
            first_name (str): student's fist name
            last_name (str): student's last name
            age (int): student's age
    """
    def __init__(self, first_name, last_name, age):
        """
            Class object initializer

            Args:
                first_name (str): item to set to first name att
                last_name (str): item to set to last name att
                age (int): value to set to age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation of a Student

            Args:
                attrs (list): list of attribute to be returned
        """
        if attrs is not None and type(attrs) is list:
            json = {}
            if len(attrs) == 0:
                return json
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
            for i in attrs:
                if i in self.__dict__.keys():
                    json[i] = self.__dict__[i]
            return json
        return self.__dict__
