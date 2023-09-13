#!/usr/bin/python3

def uniq_add(my_list=[]):
    """A function that adds all unique integers in a list."""
    unique_integers = set(my_list)
    result = sum(unique_integers)
    return (result)
