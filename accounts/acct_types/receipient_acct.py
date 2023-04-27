from abc import abstractmethod, ABC
from user_acct import User

class Receipient(User):
    
    def __init__(self, username, phone):
        # super().__init__()
        self.username = username
        self.phone = phone
        
    def createAcct(self, phone):
        self.username = (phone)[3::]
        receipient = Receipient(username=self.username, phone=phone)
        
        return receipient
        