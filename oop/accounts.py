import datetime
import pytz


# encapsulation demonstration with bank accounts
class Account:
    # Its a good habit to use the below syntax as a descriptor for
    # classes
    """ Simple account class with balance """

    # Static method (called before constructor)
    # names starting with an underscore, means that they are non-public
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transation_list = [(Account._current_time(), balance)]
        print("Account created " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transation_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transation_list.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        # since pytz produces a tuple, you can unpack the tuple with the
        # for loop
        for date, amount in self._transation_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    scott = Account("Scott", 0)
    scott.show_balance()

    scott.deposit(1000)
    # scott.show_balance()
    scott.withdraw(500)
    # scott.show_balance()
    scott.withdraw(2000)

    scott.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()