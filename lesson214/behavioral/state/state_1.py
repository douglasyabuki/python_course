"""
The State Design Pattern is a behavioral pattern
that aims to allow an object to change its behavior
when its internal state changes.
The object will appear to have changed its class.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Trying to execute pending()')
        self.state.pending()
        print('Current state: ', self.state)
        print()

    def approve(self) -> None:
        print('Trying to execute approve()')
        self.state.approve()
        print('Current state: ', self.state)
        print()

    def reject(self) -> None:
        print('Trying to execute reject()')
        self.state.reject()
        print('Current state: ', self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self):
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Payment is already pending, cannot do anything.')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Payment approved')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Payment moved back to pending')

    def approve(self) -> None:
        print('Payment is already approved, cannot do anything.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Payment rejected. Cannot move to pending.')

    def approve(self) -> None:
        print('Payment rejected. Cannot approve.')

    def reject(self) -> None:
        print('Payment rejected. Cannot reject again.')


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
