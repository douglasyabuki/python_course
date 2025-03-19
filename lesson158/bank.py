import accounts
import clients


class Bank:
    def __init__(
        self,
        agencies: list[int] | None = None,
        clients: list[clients.Person] | None = None,
        accounts: list[accounts.Account] | None = None,
    ):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _check_agency(self, account):
        if account.agency in self.agencies:
            print('_check_agency', True)
            return True
        print('_check_agency', False)
        return False

    def _check_client(self, client):
        if client in self.clients:
            print('_check_client', True)
            return True
        print('_check_client', False)
        return False

    def _check_account(self, account):
        if account in self.accounts:
            print('_check_account', True)
            return True
        print('_check_account', False)
        return False

    def _check_account_belongs_to_client(self, client, account):
        if account is client.account:
            print('_check_account_belongs_to_client', True)
            return True
        print('_check_account_belongs_to_client', False)
        return False

    def authenticate(self, client: clients.Person, account: accounts.Account):
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_account_belongs_to_client(client, account)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencies!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = clients.Client('John', 30)
    cc1 = accounts.CheckingAccount(111, 222, 0, 0)
    c1.account = cc1
    c2 = clients.Client('Doe', 18)
    cp1 = accounts.SavingsAccount(112, 223, 100)
    c2.account = cp1
    bank = Bank()
    bank.clients.extend([c1, c2])
    bank.accounts.extend([cc1, cp1])
    bank.agencies.extend([111, 222])

    if bank.authenticate(c1, cc1):
        cc1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)
