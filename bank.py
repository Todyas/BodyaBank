class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance += amount
