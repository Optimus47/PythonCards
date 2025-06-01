numbers = [3, 5, 1, 4]
numbers.sort()
print(numbers)  # [1, 3, 4, 5]
numbers.sort(key=lambda x: -x)
print(numbers)  # [5, 4, 3, 1]

words = ["яблоко", "груша", "ананас"]
longest = max(words, key=lambda w: len(w))
print(longest)  # ананас
