#!/usr/bin/python3
"""
    This module contains Square bin Rectangle bin BaseG
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This class has the base functionalities
        of a simple square

        Attributes:
            __size (int): side length of square
    """
    def __init__(self, size):
        """
            Intializes square

            Args:
                size (int): given side length
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
            Returns string format for square
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
            Measure the area of the square
        """
        return Rectangle.area(self)
