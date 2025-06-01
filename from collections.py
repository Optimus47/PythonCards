from collections import namedtuple

Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p.x, p.y)

from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)  # deque([0, 1, 2, 3, 4])

from collections import Counter

c = Counter("banana")
queue = deque(c.items())  # Преобразуем в очередь
print(queue)  # deque([('b', 1), ('a', 3), ('n', 2)])

# Обрабатываем очередь
while queue:
    char, count = queue.popleft()
    print(f"Символ: {char}, Количество: {count}")

from collections import defaultdict
dd = defaultdict(int)
dd["a"] += 3
print(dd["a"])  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})

from collections import OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

from collections import ChainMap
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
c = ChainMap(a, b)
print(c)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)
d = MyDict()
d["a"] = 1  # Setting a to 1
d["b"] = 2  # Setting b to 2
print(d)  # MyDict({'a': 1, 'b': 2})

