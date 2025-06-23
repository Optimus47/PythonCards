from typing import Protocol
'''
Protocol из модуля typing позволяет описывать интерфейсы, которые поддерживает класс,
без необходимости наследования
'''
class Greeter(Protocol):
    def greet(self) -> str:
        ...

class Person:
    def greet(self) -> str:
        return "Привет!"

def welcome(greeter: Greeter):
    print(greeter.greet())

welcome(Person())
