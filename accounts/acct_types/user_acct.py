from abc import abstractmethod, ABC

class User(ABC):
   
    @abstractmethod
    def createAcct(self):
        pass