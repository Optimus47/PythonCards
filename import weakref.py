'''
Тема 68: Введение в weakref — слабые ссылки

Модуль weakref позволяет создавать слабые ссылки на объекты,
 которые не препятствуют сборщику мусора их удалять
'''
import weakref

class MyClass:
    pass

obj = MyClass()
r = weakref.ref(obj)

print(r())  # <__main__.MyClass object at ...>
del obj
print(r())  # None
