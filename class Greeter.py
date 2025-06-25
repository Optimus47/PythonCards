'''
Тема 69: Введение в __call__ — вызываемые объекты

Метод __call__ позволяет экземплярам класса вести себя как функции
'''
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Привет, {self.name}!")

g = Greeter("Аня")
g()  # Привет, Аня!

'''
класс-счётчик, который увеличивает значение при каждом вызове экземпляра
'''
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print(self.count, end=' ')
    
c = Counter()
c()  # 1
c()  # 2
c()  # 3