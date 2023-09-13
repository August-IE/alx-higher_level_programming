#!/usr/bin/python3

def roman_to_int(roman_string):
    """A function that converts a roman numeral to an integer."""
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0
    prev_value = 0

    for i in reversed(roman_string):
        value = roman_dict.get(i, 0)

        if value == 0:
            return (0)

        if value < prev_value:
            num -= value
        else:
            num += value

        prev_value = value

    return (num)
