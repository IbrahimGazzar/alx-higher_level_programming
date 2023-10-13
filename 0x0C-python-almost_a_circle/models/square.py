#!/usr/bin/python3
"""
    This module contains the definition for
    a Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A square object based on a Rectangle

        Attributes:
            __nb_objects (int): counter for un-ided objects
            id (int): id of the square object
            __width (int): width of the square
            __height (int): height of the square
            __x (int): x position of the square
            __y (int): y position of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Intialization function of the square

            Args:
                size (int): side length of the square
                x (int): given x-position of the square
                y (int): given y-position of the square
                id (int): given id of the square
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
            Returns the formatted string representation of
            square
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                + f" - {self.width}")

    def update(self, *args, **kwargs):
        """
            Updates the attributes of square

            Args:
                args (list): unkeyworded list of inputs
                kwargs (list): keyworded list of inputs
        """
        k = ["id", "size", "x", "y"]
        if args:
            for i in range(min(len(args), len(k))):
                setattr(self, k[i], args[i])
        else:
            for i in k:
                if i in kwargs:
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """
            Returns a dictionary representation
            of square
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.size}
