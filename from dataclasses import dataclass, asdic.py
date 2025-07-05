'''
Тема 77: Введение в dataclasses.asdict и dataclasses.astuple

Когда работаешь с объектами @dataclass, часто требуется преобразовать 
их в словарь или кортеж
'''
from dataclasses import dataclass, asdict

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(asdict(p))  # {'x': 1, 'y': 2}

from dataclasses import astuple

print(astuple(p))  # (1, 2)
