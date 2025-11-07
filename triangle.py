def area(a, h):
    '''Принимает числа a и h(сторона, высота), возвращает площадь'''
    if a <= 0 or h <= 0:
        return 0
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает числа a, b, c(стороны), возвращает периметр'''
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    return a + b + c