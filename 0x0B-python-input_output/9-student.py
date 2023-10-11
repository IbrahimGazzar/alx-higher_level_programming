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

    def to_json(self):
        """
            retrieves a dictionary representation of a Student
        """
        return self.__dict__
