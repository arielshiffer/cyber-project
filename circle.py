"""
Author : Ariel Shiffer
Program name : oop task
Description : class that has circle objects
Date : 17.10.22
"""

# imports
from shape import *
from math import pi

# constants


class Circle(Shape):

    def __init__(self, rad, color):
        """
        This function is to building a circle object.
        :param rad: The radius of the circle, double.
        :param color: The color of the circle, string.
        """
        super().__init__(color, (rad ** 2) * pi, 2 * rad * pi)
