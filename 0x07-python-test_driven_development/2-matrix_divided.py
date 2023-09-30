#!/usr/bin/python3

""" This python script contains the function matrix_divided required
    for the second task in this alx project """


def matrix_divided(matrix, div):
    """
        This function takes a matrix and divides each element of the matrix
        with a given divisor

        Args:
            @matrix: list containing lists of ints or floats
            @div: an int or float to divide the contents of matrix by
    """
    typerr_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(typerr_msg)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(typerr_msg)
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(typerr_msg)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_list = []
        for j in i:
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
    return new_matrix
