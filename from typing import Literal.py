'''
Тема 75: Введение в аннотацию типов с Literal

Literal из модуля typing позволяет ограничить значение переменной или аргумента конкретными фиксированными вариантами
'''
from typing import Literal

def get_status(status: Literal["open", "closed", "pending"]) -> str:
    return f"Статус: {status}"

print(get_status("open"))    # Ок
print(get_status("unknown"))  # Ошибка на этапе проверки типов c mypy
