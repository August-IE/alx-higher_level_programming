#!/usr/bin/python3

def uppercase(str):
    """A function that prints a string in uppercase followed by a new line."""
    c = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            c += "{}".format(uppercase_char)
        else:
            c += "{}".format(char)
    print(c)
