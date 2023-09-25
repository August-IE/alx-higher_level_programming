#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """A function that prints an integer.

    Args:
        value : The integer to print.

    Returns:
        True - If value has been correctly printed 
        Otherwise - False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
