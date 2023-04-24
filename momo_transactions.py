from abc import ABC ,abstractmethod

class Transactions(ABC):
    
    @abstractmethod
    def do_transaction(self):
        pass