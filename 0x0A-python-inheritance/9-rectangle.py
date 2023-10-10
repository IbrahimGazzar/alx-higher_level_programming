#!/usr/bin/python3
"""
    Show them inheritance
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A rectangle based on base geometry

        Attributes:
            __width (int): rectangle width
            __height (int): rectangle height
    """
    def __init__(self, width, height):
        """
            Sets the main attributes of the rectangle

            Args:
                width (int): given width
                height (int): given height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
            Sets a format for printing the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
            Calculate the area of the rectangle
        """
        return self.__width * self.__height