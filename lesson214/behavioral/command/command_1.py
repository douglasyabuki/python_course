"""
Command intends to encapsulate a request as an object,
thus allowing clients to be parameterized with different requests,
queue or log requests, and support undoable operations.

It is composed of a client (orchestrates everything), an invoker (invokes the requests),
one or multiple command objects (that link the receiver and the action to be executed),
and a receiver (the object that will execute the action in the end).
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    """ Receiver - Smart Light """

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} in the {self.room_name} is ON')

    def off(self) -> None:
        print(f'{self.name} in the {self.room_name} is OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self.name} in the {self.room_name} is now {self.color}')


class ICommand(ABC):
    """ Command Interface """

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ Concrete Command """

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    """ Concrete Command """

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """ Invoker """

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('Nothing to undo')
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == "__main__":
    bedroom_light = Light('Bedroom Light', 'Bedroom')
    bathroom_light = Light('Bathroom Light', 'Bathroom')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')

    remote = RemoteController()

    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('third_button', bedroom_light_blue)
    remote.button_add_command('fourth_button', bedroom_light_red)

    remote.button_pressed('first_button')
    remote.button_undo('first_button')

    remote.button_pressed('second_button')
    remote.button_undo('second_button')

    remote.button_pressed('third_button')
    # remote.button_undo('third_button')

    remote.button_pressed('fourth_button')
    remote.button_undo('fourth_button')

    print()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
