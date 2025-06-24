class InfoMeta(type):
    def __new__(cls, name, bases, dct):
        def info(self):
            return f"Класс: {self.__class__.__name__}"
        dct["info"] = info
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=InfoMeta):
    pass

# Пример использования
if __name__ == "__main__":
    # зомби зомби зомби зомби зомби зомби зомби зомби зомби
    obj = MyClass()
    print(f"Создан объект {obj} класса {obj.__class__.__name__}")
    print(f"Метакласс объекта: {obj.__class__.__class__.__name__}")
    print(f"Метакласс метакласса: {obj.__class__.__class__.__class__.__name__}")
    print(f"Метакласс метакласса метакласса: {obj.__class__.__class__.__class__.__class__.__name__}")
    print(obj.info())  # Класс: MyClass
