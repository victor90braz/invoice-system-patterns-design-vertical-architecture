from abc import ABC, abstractmethod

class BaseInvoiceTaxCalculatorInterface(ABC):
    @abstractmethod
    def calculate_tax(self, invoice):
        pass
