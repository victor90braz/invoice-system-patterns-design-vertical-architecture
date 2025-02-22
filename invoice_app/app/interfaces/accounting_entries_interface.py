from abc import ABC, abstractmethod
from invoice_app.models.invoice import Invoice

class BaseInvoiceAccountingEntriesInterface(ABC):
    
    @abstractmethod
    def generate_entry(self, invoice: Invoice) -> dict:
  
        pass
