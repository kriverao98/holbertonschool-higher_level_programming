#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = map(lambda x: x ** 2, square_matrix_simple)
        print(new_matrix)
