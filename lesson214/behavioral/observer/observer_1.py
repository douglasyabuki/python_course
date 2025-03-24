"""
The Observer pattern aims to define a one-to-many dependency between
objects so that when one object changes state,
all its dependents are notified and updated automatically.

An observer is an object that wants to be informed,
an observable (subject) is the entity that generates information.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """ Observable """

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    """ Observable """

    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return

        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
        print()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} - object {observable_name} '
              f'has just been updated => {self.observable.state}')


class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self) -> None:
        state = self.observable.state
        print('I am the notebook and will do something else with this data', state)

    def update(self) -> None:
        self.show()


if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = Smartphone('iPhone', weather_station)
    another_smartphone = Smartphone('Another Smartphone', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(another_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '32'}
    weather_station.state = {'humidity': '90'}

    weather_station.remove_observer(another_smartphone)
    weather_station.reset_state()
