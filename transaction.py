from abc import ABC, abstractmethod

class transactions(ABC):

    @abstractmethod
    def perform_transaction(self):
        pass
