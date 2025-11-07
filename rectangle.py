def area(a, b):
    '''Принимает числа a и b(стороны), возвращает площадь'''
    if a <= 0 or b <= 0:
        return 0
    return a * b

def perimeter(a, b):
    '''Принимает числа a и b(стороны), возвращает периметр'''
    if a <= 0 or b <= 0:
        return 0
    return a + a + b + b