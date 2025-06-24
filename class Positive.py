'''
Тема 67: Введение в дескрипторы (descriptors)

Дескрипторы — это объекты, управляющие доступом к атрибутам других объектов.
Они реализуют методы __get__, __set__ и __delete__.
Пример: дескриптор для положительных значений
'''
class Positive:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Только положительные значения!")
        self.value = value

class Account:
    balance = Positive()

a = Account()
a.balance = 100
print(a.balance)  # 100
try:
    a.balance = -50  # Попытка установить отрицательное значение
except ValueError as e:
    print(e)

'''
пример дескриптора, который разрешает только значения определённого типа
и сохраняет только уникальные значения для каждого экземпляра
'''
class TypedUnique:
    def __init__(self, typ):
        self.typ = typ
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance)

    def __set__(self, instance, value):
        if not isinstance(value, self.typ):
            raise TypeError(f"Значение должно быть типа {self.typ.__name__}")
        # Проверяем уникальность среди всех экземпляров
        if value in self.data.values():
            raise ValueError("Значение должно быть уникальным!")
        self.data[instance] = value

    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]

class User:
    name = TypedUnique(str)

u1 = User()
u2 = User()
u1.name = "Alice"
u2.name = "Bob"
print(u1.name)  # Alice
print(u2.name)  # Bob

try:
    u2.name = 123  # Ошибка типа
except TypeError as e:
    print(e)

try:
    u2.name = "Alice"  # Ошибка уникальности
except ValueError as e:
    print(e)

