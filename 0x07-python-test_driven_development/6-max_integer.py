#!/usr/bin/python3
"""Interactive tests
"""


def max_integer(list=[]):
    """find and return the max integer in a list
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
