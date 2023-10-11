class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self) -> str:
        return f"Bank account owner: {self.owner}, with a balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        if amount > self.balance:
            raise ValueError("Withdrawal amount exceeds account balance")
        self.balance -= amount


acct1 = Account("Jose", 100)
print(acct1)
print(acct1.balance)
acct1.deposit(50)
acct1.withdrawal(50)
print(acct1.owner)
acct1.withdrawal(200)
print(acct1)
