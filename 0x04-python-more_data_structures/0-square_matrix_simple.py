#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrmat = []
    for i in matrix:
        sqrlst = []
        for j in i:
            sqrlst.append(j * j)
        sqrmat.append(sqrlst)
    return sqrmat
