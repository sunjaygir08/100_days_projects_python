class Account:
    def __init__(self):
        self.balance = 0
        print("New Account is Created")

    def deposit(self):
        amount=float(input("Enter the amount to deposit: "))
        self.balance += amount
        print("New balance is:", self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (amount > self.balance):
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("New balance is:", self.balance)

    def inquiry(self):
        print("Current balance is:", self.balance)

ac = Account()
ac.deposit()
ac.withdraw()
ac.inquiry()
