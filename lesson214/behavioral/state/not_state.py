# THE FOLLOWING CODE DOES NOT IMPLEMENT THE STATE DESIGN PATTERN
# IT'S AN EXAMPLE OF WHAT THE PATTERN AIMS TO SOLVE.

from __future__ import annotations
from enum import Enum, auto


class Payment(Enum):
    """
    We define an enum with the state options
    that our Order object can have
    """
    Pending = auto()
    Approved = auto()
    Rejected = auto()

    def __str__(self):
        """
        This will return the class name (Payment)
        plus the member name. Ex.: PaymentApproved
        """
        return f'{self.__class__.__name__}{self.name}'


class Order:
    def __init__(self) -> None:
        self.state: Payment = Payment.Pending

    def change_state(self, state: Payment):
        """
        THE FOLLOWING CODE DOES NOT IMPLEMENT THE STATE DESIGN PATTERN
        IT'S AN EXAMPLE OF WHAT THE PATTERN AIMS TO SOLVE.
        """

        # Pending
        if self.state == Payment.Pending and state == Payment.Pending:
            print('Payment is already pending, cannot move to pending again.')
        elif self.state == Payment.Pending and state == Payment.Approved:
            self.state = Payment.Approved
            print('Payment approved')
        elif self.state == Payment.Pending and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('Payment rejected')

        # Approved
        elif self.state == Payment.Approved and state == Payment.Approved:
            print('Payment already approved, cannot approve again.')
        elif self.state == Payment.Approved and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('Payment rejected')
        elif self.state == Payment.Approved and state == Payment.Pending:
            self.state = Payment.Pending
            print('Payment moved back to pending')

        # Rejected
        elif self.state == Payment.Rejected and state == Payment.Approved:
            print('Payment rejected. Cannot approve it')
        elif self.state == Payment.Rejected and state == Payment.Rejected:
            print('Payment rejected. Cannot reject again')
        elif self.state == Payment.Rejected and state == Payment.Pending:
            print('Payment rejected. Cannot move to pending')

        print(f'Current state: {self.state}')
        print()

    def pending(self) -> None:
        print('Trying to execute pending(Payment.Pending)')
        self.change_state(Payment.Pending)

    def approve(self) -> None:
        print('Trying to execute approve(Payment.Approved)')
        self.change_state(Payment.Approved)

    def reject(self) -> None:
        print('Trying to execute reject(Payment.Rejected)')
        self.change_state(Payment.Rejected)


if __name__ == "__main__":
    o1 = Order()
    o1.approve()
    o1.approve()
    o1.reject()
    o1.approve()
    o1.pending()
