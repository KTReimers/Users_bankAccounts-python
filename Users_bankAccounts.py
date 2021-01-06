class User:
    def __init__(self, nameInput):
        self.name= nameInput
        self.amount = 0
        self.Checking = BankAccount(0.01, 1000)
        self.Savings = BankAccount(0.05, 2000)

    def make_deposit(self, amount, ChooseAccount):
        if ChooseAccount == "Checking":
            self.Checking.deposit(amount)
        elif ChooseAccount == "Savings":
            self.Savings.deposit(amount)
        return self

    def make_withdrawl(self, amount, ChooseAccount):
        if ChooseAccount == "Checking":
            if self.amount< amount:
                print("insufficient funds")
            else:
                self.Checking.withdraw(amount)
            return self
        if ChooseAccount == "Savings":
            if self.amount< amount:
                print("insufficient funds")
            else:
                self.Savings.withdraw(amount)
            return self

    def display_User_Balance(self):
        # print(f"User name: {self.name}, Balance: ${self.amount}")
        print(f"Checking: ${self.Checking.balance}\n Savings: ${self.Savings.balance}")

    def transfer_money(self,other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        return (self)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.interest = int_rate

    def deposit(self, amount):
		# your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
		# your code here
        if self.balance<amount:
            print("no mas monies")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
		# your code here
        print(f"Current Balance: ${self.balance} ")

    def yield_interest(self):
		# your code here
        self.balance += self.interest * self.balance
        return self

user1 = User("Guido van Rossum")
# print(user1.name)
# user1.display_User_Balance()
user2 = User("Steve Goodman")
user3 = User("Billy Jones")
# Checking= BankAccount(0.01, 1000)
# Savings = BankAccount(0.01, 5000)

user1.Checking.deposit(50),user1.display_User_Balance()
# user1.display_User_Balance()
user1.Savings.withdraw(100),user1.display_User_Balance()