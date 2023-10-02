#!/usr/bin/python3
"""
    This module contains a properly defined Rectangle class
"""


class Rectangle():
    """
        This class defines a simple Rectangle object

        Attributes:
            __width (int): rectangle's width
            __height (int): rectangle's height
    """
    def __init__(self, width=0, height=0):
        """
            Initialization function for a Rectangle object

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Property to retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter for the attribute width

            Args:
                @value: value to set to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Property to retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter function for height

            Args:
                @value: value to set height to
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
