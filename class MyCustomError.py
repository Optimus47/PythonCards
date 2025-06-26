'''
Тема 71: Введение в создание собственных исключений

В Python можно создавать свои собственные типы исключений для более точной обработки ошибок
'''
class MyCustomError(Exception):
    pass

def do_something(value):
    if value < 0:
        raise MyCustomError("Значение не может быть отрицательным")

try:
    do_something(-1)
except MyCustomError as e:
    print(f"Произошла ошибка: {e}")

class InvalidUserData(Exception):
    """Исключение для некорректных данных пользователя."""
    pass

def check_user(name, age):
    if not name:
        raise InvalidUserData("Имя не может быть пустым")
    if not (0 < age < 120):
        raise InvalidUserData("Возраст должен быть от 1 до 119")

try:
    check_user("", 25)
except InvalidUserData as e:
    print(f"Ошибка пользователя: {e}")

try:
    check_user("Анна", 150)
except InvalidUserData as e:
    print(f"Ошибка пользователя: {e}")