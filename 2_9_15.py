#Program that takes in a radius and finds the area of a circle using functions

import math

def circleArea(radius):
    """The circleArea function returns the area of a circle with a given radius"""
    area = math.pi * (radius**2)
    return(area)

def main():
    radius = float(input("What is the radius?"))
    return(circleArea(radius))


print("The area is", main())

