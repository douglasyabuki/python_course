# Relationships between classes: association, aggregation, and composition
# Composition is a specialization of aggregation.
# In composition, when the "parent" object is deleted,
# all references to the "child" objects are also deleted.
class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, street, number):
        self.addresses.append(Address(street, number))

    def add_external_address(self, address):
        self.addresses.append(address)

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)

    def __del__(self):
        print('DELETING,', self.name)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print('DELETING,', self.street, self.number)


client1 = Client('Maria')
client1.add_address('Av Brasil', 54)
client1.add_address('Rua B', 6745)
external_address = Address('Av Saudade', 123213)
client1.add_external_address(external_address)
client1.list_addresses()

del client1

print(external_address.street, external_address.number)
print('######################## HERE ENDS MY CODE')
