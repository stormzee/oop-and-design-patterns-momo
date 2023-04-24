from transfer_money.transfer_money import TransferMoney
from utils.utils import confirm_transaction, get_balance

class MtnTransfer(TransferMoney):

    def __int__(self, account_number:str, amount:float, reference:str, pin:str):
        self.account_number = account_number
        self.amount = amount
        self.reference = reference
        self.pin = pin

    def do_transaction(self):
        # implement the charges later, here
        # calculate the percentage and add it to the total amount being transferred
        # eg.
        self.amount += 0.03 * self.amount
        return confirm_transaction(self.pin, self.amount)