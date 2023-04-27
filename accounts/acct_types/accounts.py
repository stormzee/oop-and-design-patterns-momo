from abc import ABC
from user_acct import User

class UserAccount(User):
    def __init__(self, sender=None, receipient=None):
        self.sender = sender
        self.receipient = receipient
        

    def createAcct(self):
        return self.sender.createAcct(self.sender.phone, self.sender.pin_code) or self.receipient.createAcct(self.receipient.phone)
 