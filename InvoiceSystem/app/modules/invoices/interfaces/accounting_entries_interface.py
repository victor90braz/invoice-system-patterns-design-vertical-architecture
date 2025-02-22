from abc import ABC, abstractmethod
from InvoiceSystem.app.modules.invoices.models.invoice import Invoice  

class BaseInvoiceAccountingEntriesInterface(ABC):
    
    @abstractmethod
    def generate_entry(self, invoice: Invoice) -> dict:
  
        pass
