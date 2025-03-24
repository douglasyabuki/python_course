"""
Factory Method is a creational pattern that allows you to define an interface for
creating objects but lets the subclasses decide which objects to create.
The Factory Method delays instantiation to subclasses, ensuring
low coupling between classes.
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


class VehicleFactory(ABC):
    def __init__(self, vehicle_type) -> None:
        self.vehicle = self.get_vehicle(vehicle_type)

    @staticmethod
    @abstractmethod
    def get_vehicle(vehicle_type: str) -> Vehicle: pass

    def pick_up_client(self) -> None:
        self.vehicle.pick_up_client()


class NorthZoneVehicleFactory(VehicleFactory):
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


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == 'economy':
            return EconomyCar()
        assert 0, 'Vehicle does not exist'


if __name__ == "__main__":
    from random import choice
    available_north_zone = ['luxury', 'economy', 'motorbike', 'luxury_motorbike']
    available_south_zone = ['economy']

    print('NORTH ZONE')
    for i in range(10):
        vehicle = NorthZoneVehicleFactory(
            choice(available_north_zone))
        vehicle.pick_up_client()

    print()

    print('SOUTH ZONE')
    for i in range(10):
        vehicle2 = SouthZoneVehicleFactory(
            choice(available_south_zone))
        vehicle2.pick_up_client()
