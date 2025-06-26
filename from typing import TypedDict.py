'''
Тема 73: Введение в аннотацию типов с TypedDict

TypedDict из модуля typing позволяет описывать словари с фиксированными полями и типами
'''
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

    @classmethod
    def validate(cls, data: dict) -> "User":
        if not isinstance(data.get("age"), int):
            raise TypeError(f"Возраст должен быть числом, а не {type(data.get('age')).__name__}")
        if not isinstance(data.get("name"), str):
            raise TypeError(f"Имя должно быть строкой, а не {type(data.get('name')).__name__}")
        return data  # type: ignore

def greet(user: User | None):
    if user is None:
        print("Нет данных о пользователе.")
    else:
        print(f"Привет, {user['name']}! Тебе {user['age']} лет.")

try:
    user1: User | None = User.validate({"name": "Аня", "age": 30})
except TypeError as e:
    print("Ошибка:", e)
    user1 = None

try:
    user2: User | None = User.validate({"name": "Борис", "age": "xx"})  # вызовет TypeError
except TypeError as e:
    print("Ошибка:", e)
    user2 = None

greet(user1)
greet(user2)
