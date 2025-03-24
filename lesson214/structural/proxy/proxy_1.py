"""
The Proxy is a structural design pattern that aims to provide a substitute object
that acts as if it were the real object the client code wants to use.
The proxy will receive the requests and control how and when to forward such
requests to the real object.

Based on how proxies are used, we classify them as:

- Virtual Proxy: controls access to resources that may be expensive to create or use.
- Remote Proxy: controls access to resources located on remote servers.
- Protection Proxy: controls access to resources that may require authentication or permission.
- Smart Proxy: in addition to controlling access to the real object, also performs
extra tasks to determine when and how to execute certain actions.

Proxies can do many things:
logging, authenticating users, service distribution,
caching, creating and destroying objects, delaying executions,
and much more...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    """ Subject Interface """

    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    """ Real Subject """

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulating request
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # Simulating request
        return [
            {'street': 'Av. Brasil', 'number': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # Simulating request
        return {
            'social_security_number': '111.111.111-11',
            'id_number': 'AB111222444'
        }


class UserProxy(IUser):
    """ Proxy """

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # These objects don't exist yet at this point
        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    luiz = UserProxy('Luiz', 'Otávio')

    # Instant response
    print(luiz.firstname)
    print(luiz.lastname)

    # Takes 6 seconds because it comes from the real subject
    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    # Instant response (because it's cached)
    print('CACHED DATA:')
    for i in range(50):
        print(luiz.get_addresses())
