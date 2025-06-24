class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Создание класса {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

# Пример использования
if __name__ == "__main__":
    # зомби зомби зомби зомби зомби зомби зомби зомби зомби
    obj = MyClass()
    print(f"Создан объект {obj} класса {obj.__class__.__name__}")
    print(f"Метакласс объекта: {obj.__class__.__class__.__name__}")
    print(f"Метакласс метакласса: {obj.__class__.__class__.__class__.__name__}")
    print(f"Метакласс метакласса метакласса: {obj.__class__.__class__.__class__.__class__.__name__}")
