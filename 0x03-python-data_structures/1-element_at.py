#!/usr/bin/python3

def element_at(my_list, idx):
    """A function that retrieves an element from a list like in C."""
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
