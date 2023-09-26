#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 3 - Square
        Create a square that can calculate its own area
"""


class Square:
    """ This a Square with a given apropriate size that can measure area

        Attributes:
              __size (int): length of the square's sides
    """
    def __init__(self, size=0):
        """ This function intializes an object of type Square

            Args:
                size (int): given side length of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
           This function can calculate square area
        """
        return self.__size * self.__size
