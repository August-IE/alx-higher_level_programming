#!/usr/bin/python3

def max_integer(my_list=[]):
    """A function that finds the biggest integer of a list."""
    if not my_list:
        return None

    max_integer = my_list[0]
    for num in my_list:
        if num > max_integer:
            max_integer = num

    return (max_integer)
