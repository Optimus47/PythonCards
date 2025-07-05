'''
Тема 79: Введение в мемоизацию

Мемоизация — это метод оптимизации, при котором результаты вызовов
функции сохраняются, чтобы повторные вызовы с теми же аргументами 
не выполняли расчёты заново.
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

'''
Ручная мемоизация
'''

cache = {}

def fib_diy(n):
    if n in cache:
        return cache[n]
    if n < 2:
        result = n
    else:
        result = fib_diy(n - 1) + fib_diy(n - 2)
    cache[n] = result
    return result

print(fib_diy(10))  # 55
