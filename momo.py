from abc import ABC
from momo_transactions import Transactions

class Momo(Transactions):
    def __init__(self, user, transaction_type):
        self.user = user
        self.transaction_type = transaction_type

    def do_transaction(self):
        return self.transaction_type.do_transaction()

