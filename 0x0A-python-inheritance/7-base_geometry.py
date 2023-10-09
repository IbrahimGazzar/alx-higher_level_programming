#!/usr/bin/python3
"""
    This module contains the somewhat empty class
    BaseGeometry
"""


class BaseGeometry:
    """
        somewhat empty class
    """
    def area(self):
        """
            Simply raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value, making sure it's an int
            and greater than 0

            Args:
                name (string): name of an attribute
                value (int): value of the attribute
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
