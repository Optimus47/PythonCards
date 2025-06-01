class Counter:
    def __init__(self, max):
        self.current = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in Counter(3):
    print(num)  # 1, 2, 3
