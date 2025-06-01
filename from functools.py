from functools import lru_cache

from functools import wraps
from time import time
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Running {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper



@lru_cache(maxsize=128)
@timeit
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))  # 55
print(fib(15))  # 610
print(fib(5))   # 5
print(fib(20))  # 6765

print(fib.cache_info())  # CacheInfo(hits=8, misses=11, maxsize=128, currsize=11)

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25

from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # 24

@timeit
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
print(slow_function(1000000))  # Function slow_function took 0.1234 seconds
