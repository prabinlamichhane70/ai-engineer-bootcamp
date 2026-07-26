# Different classes represent different payment methods.
# Each class has the same method name: pay()
# but each method has a different implementation.

class CreditCard:
    def pay(self):
        print("Payment can be done using credit card")


class PayPal:
    def pay(self):
        print("Payment can be done using paypal")


class BankTransfer:
    def pay(self):
        print("Payment can be done Bank Transfer")


class Cash:
    def pay(self):
        print("Payment can be done using cash")


# This function accepts any payment object.
# It does not care about the object's class.
# It only checks whether the object has a pay() method.
# This is an example of duck typing and polymorphism.

def process_payment(all_payment):
    all_payment.pay()


# The same function works with different objects.
# Python decides which pay() method to call at runtime
# based on the object passed to the function.

process_payment(CreditCard())
process_payment(PayPal())
process_payment(BankTransfer())
process_payment(Cash())