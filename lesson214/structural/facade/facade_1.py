"""
Facade is a structural design pattern
that aims to provide a unified interface
to a set of interfaces in a subsystem.
Facade defines a higher-level interface
that makes the subsystem easier to use.
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
        print(f'{self.name}: The {observable_name} object '
              f'has just been updated => {self.observable.state}')


class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self) -> None:
        state = self.observable.state
        print('I am the notebook and will do something else with this data', state)

    def update(self) -> None:
        self.show()


class WeatherStationFacade:
    """
    This is our facade
    """

    def __init__(self) -> None:
        self.weather_station = WeatherStation()

        self.smartphone = Smartphone('iPhone', self.weather_station)
        self.other_smartphone = Smartphone('Other Smartphone', self.weather_station)
        self.notebook = Notebook(self.weather_station)

        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.other_smartphone)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        self.weather_station.remove_observer(self.smartphone)

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'humidity': '90'})

    weather_station.remove_smartphone()
    weather_station.reset_state()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'humidity': '90'})
