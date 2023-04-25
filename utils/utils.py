#import user class here

from users import User

def confirm_transaction(transaction_code, transaction_amount):
    if User.pin_code == transaction_code and User.balance >= transaction_amount:
        User.balance -= transaction_amount
        return User.balance
    else:
        return "Transaction Failed, check your pin and or balance"

def get_balance(transaction_code):
    if User.pin_code == transaction_code:
        return User.balance
    else:
        return "Transaction Failed, check your pin"