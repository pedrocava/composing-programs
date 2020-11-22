
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    

a = Account('Pedro')
a.balance
a.holder

b = Account('Marcelo')

b.balance = 200
[acc.balance for acc in (a, b)]

class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:  
            self.balance = self.balance - amount
            return self.balance
    

b.deposit(200)
b.withdraw(75)

        