#!/usr/bin/python3
"""Module divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")

    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")

    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")

    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the\
                same size")

        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j])
            is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))

    return new_matrix
