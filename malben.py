"""
Author : Ariel Shiffer
Program name : oop task
Description : class that has malben objects
Date : 17.10.22
"""

# imports
from shape import *

# constants


class Malben(Shape):

    def __init__(self, tzela1, tzela2, color):
        """
        This function is to building a Malben object.
        :param tzela1: The length of tzela1, double.
        :param tzela2: The length of tzela2, duoble.
        :param color: The color of the malben, string.
        """
        super().__init__(color, tzela1 * tzela2, 2 * tzela1 + 2 * tzela2)
        self.tzela1 = tzela1
        self.tzela2 = tzela2

    def get_side1(self):
        """
        This function used to get the length
        of tzela1 of the malben.
        :return: the length of tzela1 of the malben, double.
        """
        return self.tzela1

    def get_side2(self):
        """
        This function used to get the length
        of tzela2 of the malben.
        :return: the length of tzela2 of the malben, double.
        """
        return self.tzela2

    def add_two_malbens(self, shape):
        """
        This function is adding two malben object to one.
        :param shape: a malben object.
        :return: The new malben (after adding the two malbens).
        """
        if self.tzela1 == shape.get_side1():
            return Malben(self.tzela1, self.tzela2 + shape.get_side2(),
                          self.color)
        elif self.tzela2 == shape.get_side1():
            return Malben(self.tzela2, self.tzela1 + shape.get_side2(),
                          self.color)
        elif self.tzela1 == shape.get_side2():
            return Malben(self.tzela1, self.tzela2 + shape.get_side1(),
                          self.color)
        elif self.tzela2 == shape.get_side2():
            return Malben(self.tzela2, self.tzela1 + shape.get_side1(),
                          self.color)
        else:
            return None
