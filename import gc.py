'''
Тема 72: Введение в менеджеры памяти — gc (сборщик мусора)

Python имеет встроенный сборщик мусора (garbage collector), который автоматически освобождает память, занятую неиспользуемыми объектами.
'''
import gc

# Принудительный запуск сборщика мусора
gc.collect()

# Получение списка объектов, которые нельзя освободить
unreachable = gc.garbage

class Node:
    def __init__(self):
        self.ref = None
    def __del__(self):
        pass  # наличие __del__ мешает gc автоматически удалять циклы

a = Node()
b = Node()
a.ref = b
b.ref = a

del a
del b

# Включаем сбор неосвобождаемых объектов
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()

print("Неосвобождаемые объекты:", gc.garbage)