"""
Adapter is a structural design pattern that
aims to allow two otherwise incompatible classes
to work together through an "adapter".
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('Moving up...')

    def right(self) -> None:
        print('Moving right...')

    def down(self) -> None:
        print('Moving down...')

    def left(self) -> None:
        print('Moving left...')


class NewControl:
    def move_top(self) -> None:
        print('NewControl: Moving up...')

    def move_right(self) -> None:
        print('NewControl: Moving right...')

    def move_down(self) -> None:
        print('NewControl: Moving down...')

    def move_left(self) -> None:
        print('NewControl: Moving left...')


class ControlAdapter:
    """ Adapter Object """

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    """ Adapter Class """

    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == "__main__":
    # Control - Adapter Object
    new_control = NewControl()
    control_object = ControlAdapter(new_control)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()
    # Control - Adapter Class
    control_class = ControlAdapter2()

    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()
