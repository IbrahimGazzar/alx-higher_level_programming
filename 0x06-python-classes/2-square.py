#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 1 - Square
    This file demonstrates putting attributes in a class
"""


class Square:
    """ This a Square with a known size

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
