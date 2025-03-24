"""
Abstract Factory is a creational pattern that provides an interface
for creating families of related or dependent objects without specifying
their concrete classes. Abstract Factory often relies on one or more
Factory Methods to create its objects.

An important difference between Factory Method and Abstract Factory
is that Factory Method uses inheritance, while Abstract Factory uses composition.

Principle: program to interfaces, not to implementations.
"""
from abc import ABC, abstractmethod


class LuxuryVehicle(ABC):
    @abstractmethod
    def pick_up_client(self) -> None: pass


class EconomyVehicle(ABC):
    @abstractmethod
    def pick_up_client(self) -> None: pass


class LuxuryCarNorth(LuxuryVehicle):
    def pick_up_client(self) -> None:
        print('Luxury car from North Zone is picking up the client...')


class EconomyCarNorth(EconomyVehicle):
    def pick_up_client(self) -> None:
        print('Economy car from North Zone is picking up the client...')


class LuxuryBikeNorth(LuxuryVehicle):
    def pick_up_client(self) -> None:
        print('Luxury bike from North Zone is picking up the client...')


class EconomyBikeNorth(EconomyVehicle):
    def pick_up_client(self) -> None:
        print('Economy bike from North Zone is picking up the client...')


class LuxuryCarSouth(LuxuryVehicle):
    def pick_up_client(self) -> None:
        print('Luxury car from South Zone is picking up the client...')


class EconomyCarSouth(EconomyVehicle):
    def pick_up_client(self) -> None:
        print('Economy car from South Zone is picking up the client...')


class LuxuryBikeSouth(LuxuryVehicle):
    def pick_up_client(self) -> None:
        print('Luxury bike from South Zone is picking up the client...')


class EconomyBikeSouth(EconomyVehicle):
    def pick_up_client(self) -> None:
        print('Economy bike from South Zone is picking up the client...')


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVehicle: pass

    @staticmethod
    @abstractmethod
    def get_economy_car() -> EconomyVehicle: pass

    @staticmethod
    @abstractmethod
    def get_luxury_bike() -> LuxuryVehicle: pass

    @staticmethod
    @abstractmethod
    def get_economy_bike() -> EconomyVehicle: pass


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarNorth()

    @staticmethod
    def get_economy_car() -> EconomyVehicle:
        return EconomyCarNorth()

    @staticmethod
    def get_luxury_bike() -> LuxuryVehicle:
        return LuxuryBikeNorth()

    @staticmethod
    def get_economy_bike() -> EconomyVehicle:
        return EconomyBikeNorth()


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarSouth()

    @staticmethod
    def get_economy_car() -> EconomyVehicle:
        return EconomyCarSouth()

    @staticmethod
    def get_luxury_bike() -> LuxuryVehicle:
        return LuxuryBikeSouth()

    @staticmethod
    def get_economy_bike() -> EconomyVehicle:
        return EconomyBikeSouth()


class Client:
    def pick_up_clients(self) -> None:
        for factory in [NorthZoneVehicleFactory(), SouthZoneVehicleFactory()]:
            economy_car = factory.get_economy_car()
            economy_car.pick_up_client()

            luxury_car = factory.get_luxury_car()
            luxury_car.pick_up_client()

            economy_bike = factory.get_economy_bike()
            economy_bike.pick_up_client()

            luxury_bike = factory.get_luxury_bike()
            luxury_bike.pick_up_client()


if __name__ == "__main__":
    client = Client()
    client.pick_up_clients()
