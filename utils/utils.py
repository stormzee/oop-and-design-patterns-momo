#import user class here

from users.users_profile import User

def confirm_transaction(transaction_code, transaction_amount) -> str:
    if User.pin_code == transaction_code and User.balance >= transaction_amount:
        User.balance -= transaction_amount
    return get_balance(transaction_code)

def get_balance(transaction_code) -> int:
    if User.pin_code == transaction_code:
        return User.balance
    else:
        return "Transaction Failed, check your pin"