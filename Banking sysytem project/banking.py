class Banking:
    def __init__(self,user_name,initial_balance):
        self.name = user_name
        self.balance = initial_balance

    def deposit (self,ammount):
        if ammount>0:
            self.balance += ammount
        return ammount

    def get_balance (self):
        return self.balance

    def withdraw (self,ammount):
        if ammount < self.balance:
            self.balance -= ammount
            return ammount
        else: return f"Insufficient Balance"


Nafiul = Banking ("Nafiul islam Noman",100000000)
print(f"Account Name: {Nafiul.name}")
print(f"Initial Balance is: {Nafiul.balance}")
print(f"Deposit Balance: {Nafiul.deposit(1000)}")
print(f"Initial Balance after deposit is: {Nafiul.get_balance()}")
print(f"Withdraw Balance: {Nafiul.withdraw(1000)}")
print(f"Initial Balance after withdraw is: {Nafiul.get_balance()}")