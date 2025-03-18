# Relationships between classes: association, aggregation, and composition
# Aggregation is a more specialized form of association
# between two or more objects. Each object will have
# its own independent lifecycle.
# It is usually a one-to-many relationship, where one
# object has one or many objects.
# The objects can live separately, but it may
# be a relationship where one object needs the
# other to perform a certain task.
# (there are controversies about the exact definition of aggregation).
class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])

    def add_products(self, *products):
        for product in products:
            self._products.append(product)

    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
p1, p2 = Product('Pen', 1.20), Product('T-Shirt', 20)
cart.add_products(p1, p2)
cart.list_products()
print(cart.total())
