from abc import ABC, abstractmethod
from decimal import Decimal
from InvoiceSystem.models import Invoice


class TaxRuleInterface(ABC):

    @abstractmethod
    def calculate_tax(self, invoice: Invoice) -> Decimal:
        pass
