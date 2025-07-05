'''
Тема 78: Введение в каррирование функций
'''
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(4))  # 16

def multiply(a):
    def inner(b):
        return a * b
    return inner

times2 = multiply(2)
print(times2(5))  # 10


