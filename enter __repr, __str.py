'''
Тема 83: Введение в __repr__ vs __str__

    __repr__ — для разработчиков (отладка), должен быть "официальным" представлением, 
               желательно таким, чтобы eval(repr(obj)) == obj

    __str__ —  для пользователя, читаемое и красивое отображение
'''
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title!r})"

    def __str__(self):
        return f"Книга: {self.title}"

b = Book("1984")
print(repr(b))  # Book('1984')
print(str(b))   # Книга: 1984
print(b)

