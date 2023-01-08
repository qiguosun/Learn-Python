# Method Overridding: replacing or extending a method defined in the base clase
class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1  # attributes can be inherited

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
