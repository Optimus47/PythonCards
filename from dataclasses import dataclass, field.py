'''
Тема 76: Введение в dataclasses.field для настройки полей

Когда создаёшь классы с @dataclass, с помощью field() можно управлять поведением отдельных полей
'''
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
    active: bool = field(default=True)
    id: int = field(init=False)

    def __post_init__(self):
        self.id = hash(self.name)

u1 = User(name="Анна")
u2 = User(name="Борис", tags=["python", "dev"], active=False)

u1.tags.append("student")
print(u1)  # User(name='Анна', tags=['student'], active=True, id=...)
print(u2)  # User(name='Борис', tags=['python', 'dev'], active=False, id=...)

print(u1.tags)  # ['student']
print(u2.tags)
