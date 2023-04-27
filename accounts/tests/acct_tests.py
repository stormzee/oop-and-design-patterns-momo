import unittest
from acct_types import accounts, receipient_acct, sender_acct
class TestUserAccounts(unittest.TestCase):
    def test_sender_creation(self):
        username = 'sam'
        phone = '02014586556'
        pin_code = 1998
        
        # create two sender users and check whether their instance creation is similar
        # ie., whther the were created from the same class
        created_user1= sender_acct.Sender(username, phone, pin_code)
        created_user2 = sender_acct.Sender(username, phone, pin_code)
        self.assertTrue(isinstance(created_user1, sender_acct.Sender()), isinstance(created_user2, sender_acct.Sender()))




if __name__ == "__main__":
    unittest.main()
    