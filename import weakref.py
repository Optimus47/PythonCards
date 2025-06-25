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

'''
использовать weakref.WeakValueDictionary для хранения объектов,
 которые должны удаляться при отсутствии других ссылок
'''

class MyOtherClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"MyOtherClass({self.name!r})"

storage = weakref.WeakValueDictionary()

obj1 = MyOtherClass("obj1")
obj2 = MyOtherClass("obj2")

storage["first"] = obj1
storage["second"] = obj2

print(dict(storage))  # {'first': MyOtherClass('obj1'), 'second': MyOtherClass('obj2')}
del obj1
print(dict(storage))  # {'second': MyOtherClass('obj2')}

del obj2
print(dict(storage))  # {}    

