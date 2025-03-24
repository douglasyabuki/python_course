"""
In OOP, the term factory refers to a class or method
that is responsible for creating objects.

Advantages:
    Allows building a system with low coupling between classes because
    it hides the object creation logic from the client code.

    Makes it easier to add new classes to the code, since the client
    does not know or use the actual implementation (it uses the factory).

    Can help with caching or singleton creation because the
    factory may return an existing object instead of always
    creating new instances for the client.

Disadvantages:
    Can introduce too many classes in the codebase.

We will look at 2 GoF Factory types: Factory Method and Abstract Factory.

In this example:
Simple Factory <- A kind of parameterized Factory Method.
Simple Factory may not be considered a "formal" design pattern.
Simple Factory may violate some SOLID principles.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def pick_up_client(self) -> None: pass


class LuxuryCar(Vehicle):
    def pick_up_client(self) -> None:
        print('Luxury car is picking up the client...')


class EconomyCar(Vehicle):
    def pick_up_client(self) -> None:
        print('Economy car is picking up the client...')


class LuxuryMotorbike(Vehicle):
    def pick_up_client(self) -> None:
        print('Luxury motorbike is picking up the client...')


class EconomyMotorbike(Vehicle):
    def pick_up_client(self) -> None:
        print('Economy motorbike is picking up the client...')


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == 'luxury':
            return LuxuryCar()
        if vehicle_type == 'economy':
            return EconomyCar()
        if vehicle_type == 'motorbike':
            return EconomyMotorbike()
        if vehicle_type == 'luxury_motorbike':
            return LuxuryMotorbike()
        assert 0, 'Vehicle does not exist'


if __name__ == "__main__":
    from random import choice
    available_vehicles = ['luxury', 'economy', 'motorbike']

    for i in range(10):
        vehicle = VehicleFactory.get_vehicle(choice(available_vehicles))
        vehicle.pick_up_client()
