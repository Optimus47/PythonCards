from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Person:
    name: str
    age: int = field(default=18)

p = Point(1, 2)
print(p)  # Point(x=1, y=2)

p2 = Person("Анна")
print(p2)  # Person(name='Анна', age=18)