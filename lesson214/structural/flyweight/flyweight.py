"""
Flyweight is a structural design pattern
that aims to use sharing to efficiently support
large amounts of fine-grained objects.

Only use Flyweight when ALL of the following
conditions are true:

- An application uses a large number of objects;
- The storage costs are high due to the large number
of objects;
- Most object states can become extrinsic;
- Many objects can be replaced by a few shared objects;
- The application does not depend on the unique identity of objects.

Important:
- Intrinsic state is the state of the object that does not change,
this state should be inside the flyweight object;
- Extrinsic state is the state of the object that changes,
this state can be moved outside the flyweight object.

Glossary:
Intrinsic - that which is part of or constitutes the
essence or nature of something; inherent.
Extrinsic - that which does not belong to the essence of something;
that which is external.
"""
from __future__ import annotations
from typing import List, Dict


class Client:
    """Context"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """Flyweight"""

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighbourhood, address_details,
            self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Reusing existing object')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Creating new object')

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    a2 = address_factory.get_address(
        street='Av Brasil ',
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'House'
    luiz.add_address(a1)
    luiz.list_addresses()

    joana = Client('Joana')
    joana.address_number = '250A'
    joana.address_details = 'APT 555'
    joana.add_address(a2)
    joana.list_addresses()

    print(a1 == a2)
