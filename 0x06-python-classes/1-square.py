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
    def __init__(self, size):
        """ This function intializes an object of type Square

            Args:
                size (int): given side length of the square
        """
        self.__size = size
