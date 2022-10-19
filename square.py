"""
Author : Ariel Shiffer
Program name : oop task
Description : class that has square objects
Date : 17.10.22
"""

# imports
from shape import *

# constants


class Square(Shape):

    def __init__(self, tzela, color):
        """
        This function is to building a square object.
        :param tzela: The length of the tzela, double.
        :param color: The color of the square.
        """
        super().__init__(color, tzela ** 2, 4 * tzela)
