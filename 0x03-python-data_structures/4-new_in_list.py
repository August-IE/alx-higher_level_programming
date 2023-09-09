#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """A function that replaces an element in a copied list at a specific
    position without modifying the original list (like in C)."""
    if 0 <= idx < len(my_list):
        copy = [x for x in my_list]
        copy[idx] = element
        return copy
    else:
        return None
