#!/usr/bin/python3

def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format().

    Args:
        value : The integer or string to print.

    Returns:
        If value has been correctly printed - True.
        Otherwise - false.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
