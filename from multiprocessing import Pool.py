from multiprocessing import Pool
from time import sleep
import random

def square(x):
    sleep(random.uniform(0.1, 1.5))  # Имитация задержки
    print("square function called with", x)
    return x * x

if __name__ == "__main__":
    data = list(range(1, 11))  # Массив значений от 1 до 10
    with Pool(4) as pool:
        results = pool.map(square, data)
    print(f"Входные данные: {data}")
    print(f"Результаты: {results}")
