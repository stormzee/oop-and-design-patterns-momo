from abc import ABC
from transactions import transactions

class momo(transactions):
    balance = 0
    def __init__(self, phone_number, username, mm_pin):
        self.phone_number = phone_number
        self.username = username
        self.mm_pin = mm_pin


    def perform_transaction(self):
        pass

