from momo import Momo
from transfer_money.mtn_transfer import MtnTransfer
from users import User

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class MomoFactory:
    
    @staticmethod
    def create_mtnTransfer(recipient_number:str, amount:float, reference:str, pin:str):
        transfer = MtnTransfer(recipient_number, amount, reference, pin)
        user = User(username='sa', phone='02255545', pin_code='1233')
        mtntransfer_transaction = Momo(user, transfer)
        return mtntransfer_transaction
    
    