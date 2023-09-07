#!/usr/bin/python3

"""A program that imports functions from a given file, does some Maths,
    prints the result."""

a = 10
b = 5

if __name__ == "__main__":

    import calculator_1

    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
