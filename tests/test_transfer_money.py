import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from users.users import User
from transfer_money.mtn_transfer import MtnTransfer


class TestMoneytransfer(unittest.TestCase):
    
    def test_mtnTransfer(self):
        # create a user object
        # use user obj to perform a transfer
        
        user = User('sammy', '0240080134', pin_code=2000)
        recipient_number = 'kajskdnals'
        amount = 200
        pin = 2000
        transfer = MtnTransfer(user.username, user.phone, user.pin_code)
        transfer.recipient_number = recipient_number
        transfer.amount = amount
        transfer.pin = pin
        self.assertEqual(transfer.do_transaction(), 794)
        
if __name__ == "__main__":
    unittest.main()