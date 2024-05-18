#!/usr/bin/python3
"""Computes the square value of all ints in a matrix"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square of each element in a matrix.

    Args:
        matrix (list): The input matrix.

    Returns:
        list: A new matrix with the square of each element.
    """
    new_matrix = []
    
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)
    return new_matrix
