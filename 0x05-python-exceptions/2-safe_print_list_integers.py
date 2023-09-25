#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only integers

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to access in my_list.

    Returns:
        The real number of integers printed.
    """
    result = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (result)
