#!/usr/bin/python3

def uppercase(str):
    """A function that prints a string in uppercase followed by a new line."""
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            print("{}".format(c), end="")
    print("")
