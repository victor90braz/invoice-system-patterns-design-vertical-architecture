from abc import ABC, abstractmethod

class BaseTaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, invoice):
        pass
