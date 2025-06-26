'''
Тема 70: Введение в property как способ создания управляемых атрибутов

Декоратор @property позволяет создать методы, 
которые выглядят как обычные атрибуты
'''
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = value

c = Circle(5)
print(c.radius)  # 5
c.radius = 10    # корректно
# c.radius = -3  # вызовет ValueError
