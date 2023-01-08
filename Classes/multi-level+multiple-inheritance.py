# limit the inheritance within 1-2 level

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chichen(Bird):
    pass

# multiple inheritance
# if the inheirated classes don't have things in common, multiple inheritance is fine.
# Otherwise, it may raise error.


class Employee:
    def greet(self):
        print("Employee Greet")


class person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, person):
    pass


manager = Manager()
manager.greet()
