import unittest
from users import User
from transfer_money.mtn_transfer import MtnTransfer
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class transfer_money(unittest.TestCase):
    
    def test_mtnTransfer(self):
        # create a user object
        # use user obj to perform a transfer
        
        user = User('sammy', '0240080134', pin_code='2000')
        transfer = MtnTransfer(recipient_number='kajskdnals', amount= 200, pin= '2000')
        self.assertEqual(user.balance, 1800)