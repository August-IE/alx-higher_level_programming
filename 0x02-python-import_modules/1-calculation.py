#!/usr/bin/python3

"""A program that imports functions from a given file, does some Maths,
    prints the result."""

a = 10
b = 5

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
