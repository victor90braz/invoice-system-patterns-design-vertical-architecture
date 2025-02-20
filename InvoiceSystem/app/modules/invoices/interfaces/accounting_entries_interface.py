from abc import ABC, abstractmethod
from InvoiceSystem.models import Invoice  # Importing the Invoice model

class BaseInvoiceAccountingEntriesInterface(ABC):
    @abstractmethod
    def generate_entry(self, invoice: Invoice) -> dict:
        """
        Method to generate the accounting entry for the given invoice.
        
        :param invoice: The invoice object containing the data
        :return: A dictionary representing the accounting entry
        """
        pass
