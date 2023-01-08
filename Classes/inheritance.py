# Dry: don't repeat yourself!
# Inheritance: a mechanism that allows us to define the common behavior or common functions in one class,
# and then inherit them in other classes

class Animal:
    def __init__(self):
        self.age = 1  # attributes can be inherited

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
