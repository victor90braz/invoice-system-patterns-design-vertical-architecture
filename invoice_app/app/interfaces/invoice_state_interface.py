from abc import ABC, abstractmethod
from invoice_app.models.invoice import Invoice  

class BaseInvoiceStateInterface(ABC):

    @abstractmethod
    def approve(self, invoice: Invoice):
        pass

    @abstractmethod
    def cancel(self, invoice: Invoice):
        pass

    @abstractmethod
    def pay(self, invoice: Invoice):
        pass

    @abstractmethod
    def validate_transition(self, invoice: Invoice, target_state: str):
        pass
