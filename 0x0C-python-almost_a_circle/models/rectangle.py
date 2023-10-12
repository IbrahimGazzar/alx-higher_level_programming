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
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

