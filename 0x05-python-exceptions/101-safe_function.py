#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """A function that executes a function safely.

    Args:
        fct: The pointer to the function.
        args: Arguments for fct.

    Returns:
        The result of the function to fct.
        Otherwise - None.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return (None)
