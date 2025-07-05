'''
Тема 80: Введение в генераторы выражений (generator expressions)

Генераторы выражений не создают список в памяти
'''
squares = (x**2 for x in range(2,5))

print(next(squares))  # 0
print(next(squares))  # 1

print(sum(squares))


