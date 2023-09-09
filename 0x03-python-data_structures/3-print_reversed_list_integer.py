#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list in reverse order."""
    if my_list is not None and type(my_list) is list:
        reversed_list = my_list[::-1]
        for num in reversed_list:
            print("{:d}".format(num))
