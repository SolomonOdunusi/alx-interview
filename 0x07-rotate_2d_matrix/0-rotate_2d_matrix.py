#!/usr/bin/python3
"""This module rotates the matrix"""


def rotate_2d_matrix(matrix):
    """This function rotates
    a two dimensional matrix"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
