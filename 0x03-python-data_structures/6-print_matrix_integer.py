#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers."""
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d} ".format(num), end="")
