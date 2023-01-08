# not necessary need a base clase like UIControl as python is dynamic language that
# doesn't check the type of objects in a iterable list.
# it only look for the existence of certain methods in the objects.


from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
