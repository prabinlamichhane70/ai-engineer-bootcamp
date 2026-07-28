#simple example without abstract

class Car:
    def engine_start(self):
        self.__connect_key()
        print("Engine is Starting")

    
    def __connect_key(self):
        print("Connecting to engine..........")


c1 = Car()
c1.engine_start()


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")

b1 = BankAccount(3000)
b1.show_balance()
b1.deposit(2000)
b1.show_balance()
b1.withdraw(1000)
b1.show_balance()