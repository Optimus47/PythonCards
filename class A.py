class A:
    def greet(self):
        print("Привет от A")

class B:
    def greet(self):
        print("Привет от B")

class C(A,B):
    pass

c = C()
c.greet()  # Привет от A — метод разрешается по MRO (порядок наследования)

class Base:
    def say(self):
        print("Base")

class Child(Base):
    def say(self):
        super().say()
        print("Child")

Child().say()
