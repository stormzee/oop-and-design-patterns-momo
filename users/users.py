
class User:
    
    
    def __init__(self, username, phone, pin_code, balance=1000):
        self.username = username
        self.phone = phone
        self.balance = balance
        self.pin_code = pin_code
        
    def check_wallet(self, transaction_amount, transaction_pin):
        self.transaction_amount = transaction_amount
        self.transaction_pin = transaction_pin
        return self.transaction_pin == self.pin_code and self.balance >= self.transaction_amount