from abc import ABC, abstractmethod
from decimal import Decimal

class TaxRuleInterface(ABC):
    @abstractmethod
    def calculate_tax(self, amount: Decimal) -> Decimal:
        pass

