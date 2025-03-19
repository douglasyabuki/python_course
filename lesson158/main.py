"""
Exercise with Abstraction, Inheritance, Encapsulation, and Polymorphism

Create a simple banking system that has clients, accounts, and
a bank. The idea is that a client has an account (savings or checking) and
can withdraw/deposit into this account. Checking accounts have an extra limit.

Account (ABC)
    CheckingAccount
    SavingsAccount

Clients
    Client
        Client -> Account (one to one or one to many)

Bank
    Bank -> Client
    Bank -> Account

Tips:
Create a Client class that inherits from the Person class (Inheritance)
    Person has name and age (with getters)
    Client HAS an account (Aggregation from the CheckingAccount or SavingsAccount class)
Create CheckingAccount and SavingsAccount classes that inherit from Account
    CheckingAccount should have an extra limit
    Accounts have agency, account number, and balance
    Accounts must have a deposit method
    Account (superclass) must have an abstract withdraw method (Abstraction and
    polymorphism - subclasses will implement the withdraw method)
Create a Bank class to AGGREGATE clients and accounts classes (Aggregation)
The bank will be responsible for authenticating the client and accounts as follows:
    Bank has accounts and clients (Aggregation)
    * Check if the agency belongs to the bank
    * Check if the client belongs to the bank
    * Check if the account belongs to the bank
Withdrawal will only be allowed if authenticated by the bank (as described above)
Bank authenticates via a method (authenticate).
"""
import accounts
import clients
from bank import Bank

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
