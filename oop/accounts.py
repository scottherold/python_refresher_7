# encapsulation demonstration with bank accounts
class Account:
    # Its a good habit to use the below syntax as a descriptor for
    # sclasses
    """ Simple account class with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self. balance -= amount
        else:
            print("Amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print(("Balance is {}".format(self.balance)))

if __name__ == '__main__':
    scott = Account("Scott", 0)
    scott.show_balance()

    scott.deposit(1000)
    # scott.show_balance()
    scott.withdraw(500)
    # scott.show_balance()
    scott.withdraw(2000)