#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 6 - Square
        Create a square that can calculate its own area
        It can also be printed on screen, with the ability to
        manipulate its position
"""


class Square:
    """ This a Square with a given apropriate size that can measure area

        Attributes:
              __size (int): length of the square's sides
              __position ((int, int)): position of the square on screen
    """
    def __init__(self, size=0, position=(0, 0)):
        """ This function intializes an object of type Square

            Args:
                size (int): given side length of the square
                position ((int, int)): given position to manipulate
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """
            setter for the size attribute
            Args:
                 size (int):square side length
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
            getter for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter for position
            Args:
                 value ((int, int)): value of position
        """
        if not isinstance(position, (int, int)) or position[0] < 0\
           or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
           This function can calculate square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
            print a silly square

            and use the position variable to manipulte the square's poisition
        """
        for i in range(0, self.position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
