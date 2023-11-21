#!/usr/bin/python3
"""define square"""


class Square:
    """type class square

    Attributes:
    ___size (int): size of a side of the square
    """

    def __init__(self, size):
        """Initialise the square class
        Args:
        param1: size is type int attribute to make it private
        """
        self.__size = size
