class Person:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Анна", 30)
p.city = "Москва"  # AttributeError
print(p.__dict__)  # {'name': 'Анна', 'age': 30, 'city': 'Москва'}
