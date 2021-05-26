#!/usr/bin/python3
"""
    function that divides all elements of a matrix

    prototype: def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for lis in matrix:
        if type(lis) != list:
            raise TypeError(error1)
        new_matrix.append([])

    for index in range(len(matrix)):
        for i in matrix[index]:
            if type(i) is not int and type(i) is not float:
                raise TypeError(error1)
            new_matrix[index].append(round(i / div, 2))

    for x in matrix:
        if len(matrix[0]) != len(x):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return new_matrix
