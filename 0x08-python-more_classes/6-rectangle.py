#!/usr/bin/python3
"""
    This module contains a properly defined Rectangle class
    that has a public class attribute
    with additional functions for area and perimeter measurement
    and a __str__ function for display purposes
    and a proper __repr__ for recreation
    and unique (sad) farewell message on deletion
"""


class Rectangle():
    """
        This class defines a simple Rectangle object

        Attributes:
            __width (int): rectangle's width
            __height (int): rectangle's height
            number_of_instances (int): public class attribute
                that counts the number of current instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Initialization function for a Rectangle object

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """
            Define a string representation for the rectangle
        """
        string = ""
        for i in range(0, self.__height):
            if self.__width == 0:
                break
            for j in range(0, self.__width):
                string += "#"
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
            Return a string representation of the rectangle
            that can be recreated using eval()
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
            + ")"

    def __del__(self):
        """
            Handles the deletion of rectangle
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """
            Measures the rectangle's area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Measures the rectangle's perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
