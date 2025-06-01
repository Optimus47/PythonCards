import time

class MyContext:
    def __enter__(self):
        print("Вход в контекст")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выход из контекста")

with MyContext():
    print("Внутри блока")

def my_decorator(func):
    def wrapper():
        print("Перед вызовом засекаю время")
        start_time = time.time()
        func()
        print("После вызова, функция отработала")
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} секунд")
    return wrapper

@my_decorator
def say_hello():
    time.sleep(1)
    print("Привет!")

say_hello()
