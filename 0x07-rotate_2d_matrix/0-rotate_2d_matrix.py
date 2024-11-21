#!/usr/bin/python3
""" Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """ rotates a given 2D matrix 90 degrees clockwise,
        do not return anything. the matrix must be edited
        in-place
    """
    old = []
    for i in matrix:
        old.append(i.copy())
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[j][i] = old[n - i - 1][j]
