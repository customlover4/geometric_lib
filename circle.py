import math


def area(r):
    '''Принимает число r(радиус), возвращает площадь'''
    if r <= 0:
        return 0
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r(радиус), возвращает периметр'''
    if r <= 0:
        return 0
    return 2 * math.pi * r

