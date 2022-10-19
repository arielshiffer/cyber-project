"""
Author : Ariel Shiffer
Program name : oop task
Description : basic function to all the other classes
Date : 17.10.22
"""

# imports


# constants


class Shape:
    def __init__(self, color, area, perimeter):
        """
        This function builds a object from the class shape.
        :param color: string, the color of the shape.
        :param area: double, the area of the shape.
        :param perimeter: double, the area of the shape.
        """
        self.color = color
        self.area = area
        self.perimeter = perimeter

    def get_color(self):
        """
        This function is to get the color of the shape.
        :return: The color of the shape, type string.
        """
        return self.color

    def get_area(self):
        """
        This function is used to get the area of the shape.
        :return: The area of the shape, double.
        """
        return self.area

    def get_perimeter(self):
        """
        This function is used to get the area of the shape.
        :return: The area of the shape, double.
        """
        return self.perimeter

    def set_color(self, color):
        """
        This function gets a color from the user
        and changes the color of the shape.
        :param color: color you want to change the current
        color of the shape to, string.
        """
        self.color = color
