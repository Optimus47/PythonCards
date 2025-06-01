import timeit

print(timeit.timeit("sum(range(100000))", number=1000))

import cProfile

def test():
    total = 0
    for i in range(1000000):
        total += i
    total+=sum(range(1000000))

    return total

cProfile.run('test()')
