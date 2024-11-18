class Bank:
    def __init__(self, db):
        self.db = db

    def deposit(self, amount, user):
        user.balance += amount
        self.db.session.commit()

    def withdraw(self, amount, user):
        if user.balance >= amount:
            user.balance -= amount
            self.db.session.commit()
        else:
            raise ValueError("Insufficient funds")
