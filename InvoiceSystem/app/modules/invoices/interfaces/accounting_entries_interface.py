from abc import ABC, abstractmethod
from InvoiceSystem.models import Invoice  # Importing the Invoice model

class BaseInvoiceAccountingEntriesInterface(ABC):
    
    @abstractmethod
    def generate_entry(self, invoice: Invoice) -> dict:
  
        pass
