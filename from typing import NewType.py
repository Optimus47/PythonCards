'''
Тема 74: Введение в аннотацию типов с NewType

NewType из модуля typing позволяет создавать новые именованные типы 
для повышения читаемости и безопасности кода

mypy — это статический анализатор типов для Python.

Он проверяет соответствие типов в вашем коде аннотациям типов (type hints), не выполняя сам код.
mypy помогает находить ошибки, связанные с неправильным использованием типов, ещё до запуска программы.

Установите mypy:
pip install mypy
Проверьте файл:
mypy your_file.py
'''
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user_name(user_id: UserId) -> str:
    return f"Пользователь {user_id}"

uid = UserId("vvbb-1234")
print(get_user_name(uid))
