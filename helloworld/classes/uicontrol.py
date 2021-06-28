from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(args):
        print("TextBox")


class DropDownList(UIControl):
    def draw(args):
        print("DropDownList")


class Pointer():
    def point(self):
        print("I'm a point")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
point = Pointer()
draw([ddl, textbox, point])
