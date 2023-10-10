#!/usr/bin/python3
"""A function that returns a Python data structure through a JSON string."""
import json


def from_json_string(my_str):
    """Returns an object in JSON string."""
    return json.loads(my_str)
