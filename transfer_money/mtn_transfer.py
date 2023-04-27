import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from transfer_money.transfer_money import TransferMoney
from utils.utils import confirm_transaction
from users import User

class MtnTransfer(TransferMoney, User):
    
    # note that the User class inherited takes precedence over this class' variables
    '''
    MtnTransfer class inherits from the Abstract TransferMoney class and also the
    User class (whose variables take precedence over the MtnTransfer class since It is not an abstract class)
    To let the MtnTransfer class' variables take precedence as intended in the code below (but doest work as intended):
    I think you should make the MtnTransfer class a super class by using the 'super' method
    '''


    def __int__(self, recipient_number, amount, pin):
        self.recipient_number = recipient_number
        self.amount = amount
        self.pin = pin

    def do_transaction(self):
        self.amount += 0.03 * self.amount
        if self.check_wallet(self.amount, self.pin):
            self.balance -= self.amount
            return self.balance
        else:
            return "Transfer Failed"
        