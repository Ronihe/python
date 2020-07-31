class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amt):
        self.balance += amt

    def withdrawal(self, amt):
        if self.balance < amt:
            return False
        self.balance -= amt


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interest_amount(self):
        return self.balance * self.interestRate / 100
