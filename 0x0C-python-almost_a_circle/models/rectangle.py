#!/usr/bin/python3
"""
    This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
        A simple class representing a Rectangle

        Attributes:
            __nb_objects (int): counter of un-ided objects
            __width (int): width of the rectangle
            __height (int): height of the rectangle
            __x (int): x-axis position of the rectangle
            __y (int): y-axis position of the rectangle
            id (int): id of the object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Intializer of a Rectangle object

            Args:
                width (int): input width
                height (int): input height
                x (int): x position
                y (int): y position
                id (int): optional custom id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """
            Returns standard string representation
            of our rectangle object
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                + f"{self.__width}/{self.__height}")

    def area(self):
        """
            Returns the rectangle's area
        """
        return self.__width * self.__height

    def display(self):
        """
            Displays the rectangle object with hashes
        """
        for i in range(self.__height):
            for i in range(self.__width):
                print("#", end='')
            print()
