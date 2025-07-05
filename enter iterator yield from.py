'''
Тема 81: Введение в итераторы с yield from

yield from — это синтаксический сахар, который позволяет делегировать
часть генерации значений другому генератору или итерируемому объекту
'''
def gen1():
    yield from [1, 2, 3]

def gen2():
    yield 0
    yield from gen1()
    yield 4

for x in gen2():
    print(x)


