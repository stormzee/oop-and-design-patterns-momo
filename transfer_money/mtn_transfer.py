import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from transfer_money.transfer_money import TransferMoney
from utils.utils import confirm_transaction

class MtnTransfer(TransferMoney):

    def __int__(self, recipient_number, amount, pin):
        self.recipient_number = recipient_number
        self.amount = amount
        self.pin = pin

    def do_transaction(self):
        self.amount += 0.03 * self.amount
        return confirm_transaction(self.pin, self.amount)