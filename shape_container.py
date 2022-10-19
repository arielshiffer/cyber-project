"""
Author : Ariel Shiffer
Program name : oop task
Description : This code is for making a class that
can hold many shape objects.
Date : 17.10.22
"""

# imports
import random
from shape import *
from circle import *
from square import *
from malben import *

# constants
COLOR_LIST = ['Red', 'Blue', 'Green' ,'Yello', 'Orange', 'Black', 'White']
MIN_TZELA = 1
MAX_TZELA = 15



class Container:
    def __init__(self):
        """
        This function is building a container object.
        """
        self.list_of_shapes = []


    def generate(self, x):
        """
        This functions is building x number of random shapes and
        adds them to the container.
        :param x: The number of random shapes this function builds, int.
        :return: None.
        """
        i = 0
        while i < x:
            random_shape = random.randint(0,3) # 0 -> circle, 1 -> square, 2 -> malben
            random_color = random.choice(COLOR_LIST)
            if random_shape == 0:
                self.list_of_shapes.append( Circle(random.randint(MIN_TZELA,MAX_TZELA),
                                                   random_color) )
            elif random_shape == 1:
                self.list_of_shapes.append( Square(random.randint(MIN_TZELA,MAX_TZELA),
                                                   random_color) )
            elif random_shape == 2:
                self.list_of_shapes.append( Malben(random.randint(MIN_TZELA,MAX_TZELA),
                                                   random.randint(MIN_TZELA,MAX_TZELA),
                                                   random_color) )
            i += 1


    def sum_areas(self):
        """
        This function adds all the areas of the shapes that are
        in the container.
        :return: The sum of all the areas.
        """
        sum = 0
        if len(self.list_of_shapes) > 0:
            for shape in self.list_of_shapes:
                sum += shape.get_area()
        return sum


    def sum_perimeters(self):
        """
        This function adds all the perimeters of the shapes that are
        in the container.
        :return: The sum of all the perimeters.
        """
        sum = 0
        if len(self.list_of_shapes) > 0:
            for shape in self.list_of_shapes:
                sum += shape.get_perimeter()
        return sum


    def count_colors(self):
        """
        This function going through the shapes in the container
        and caculates the amount of shapes having each color.
        :return: a dictionary that holds each color as keys
        and their value is the amount of shapes in that color.
        """
        color_dict = {'Red': 0, 'Blue': 0, 'Green': 0 ,'Yello': 0, 'Orange': 0,
                      'Black': 0, 'White': 0}
        if len(self.list_of_shapes) > 0:
            for shape in self.list_of_shapes:
                for color in color_dict:
                    if shape.get_color() == color:
                        color_dict[color] = color_dict[color] + 1
        return color_dict

def main():
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    c = Container()
    c.generate(10)
    assert c.sum_areas() > 0
    assert c.sum_perimeters() > 0
    assert len(c.count_colors().values()) > 0
    main()
