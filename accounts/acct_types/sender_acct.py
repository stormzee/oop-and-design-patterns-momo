from abc import abstractmethod, ABC
from acct_types import User

class Sender(User):
    
    def __init__(self, username, phone, pin_code, balance):
        # super().__init__()
        self.username = username
        self.phone = phone
        self.pin_code = pin_code
        self.balance = balance = 1000
        
    def createAcct(self, phone, pin_code):
        self.username = (phone+"_"+ (0.314213458*pin_code))[::-7]
        sender = Sender(username=self.username, phone=phone, pin_code=pin_code,)
        
        return sender
        