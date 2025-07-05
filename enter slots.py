'''
Тема 82: Введение в __slots__ и экономию памяти в классах

__slots__ — это способ ограничить доступные атрибуты экземпляра
            класса и уменьшить использование памяти

          + высокая производительность и фиксированный набор полей
'''
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(p.x, p.y)  # 1 2

# p.z = 3  # AttributeError: 'Point' object has no attribute 'z'

