from itertools import count

for i in count(5):
    print(i)
    if i >= 10:
        break

from itertools import cycle

for i, val in enumerate(cycle("AB")):
    print(val)
    if i > 3:
        break

from itertools import chain

print(list(chain([1, 2], [3, 4])))  # [1, 2, 3, 4]

from itertools import combinations

for i in combinations("ACAB", 2):
    print(i)

from itertools import permutations

for i in permutations("ABCD", 1):
    print(i)