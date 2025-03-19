import abc


class Account(abc.ABC):
    def __init__(self, agency: int, account: int, balance: float = 0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, amount: float) -> float: ...

    def deposit(self, amount: float) -> float:
        self.balance += amount
        self.details(f'(DEPOSIT {amount})')
        return self.balance

    def details(self, msg: str = '') -> None:
        print(f'Your balance is {self.balance:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.balance!r})'
        return f'{class_name}{attrs}'


class SavingsAccount(Account):
    def withdraw(self, amount):
        post_withdraw_balance = self.balance - amount

        if post_withdraw_balance >= 0:
            self.balance -= amount
            self.details(f'(WITHDRAW {amount})')
            return self.balance

        print('Withdrawal denied')
        self.details(f'(WITHDRAWAL DENIED {amount})')
        return self.balance


class CheckingAccount(Account):
    def __init__(
        self, agency: int, account: int,
        balance: float = 0, limit: float = 0
    ):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, amount: float) -> float:
        post_withdraw_balance = self.balance - amount
        max_limit = -self.limit

        if post_withdraw_balance >= max_limit:
            self.balance -= amount
            self.details(f'(WITHDRAW {amount})')
            return self.balance

        print('Withdrawal denied')
        print(f'Your overdraft limit is {-self.limit:.2f}')
        self.details(f'(WITHDRAWAL DENIED {amount})')
        return self.balance

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.balance!r}, '\
            f'{self.limit!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    sa1 = SavingsAccount(111, 222)
    sa1.withdraw(1)
    sa1.deposit(1)
    sa1.withdraw(1)
    sa1.withdraw(1)
    print('##')
    ca1 = CheckingAccount(111, 222, 0, 100)
    ca1.withdraw(1)
    ca1.deposit(1)
    ca1.withdraw(1)
    ca1.withdraw(1)
    ca1.withdraw(98)
    ca1.withdraw(1)
    print('##')
