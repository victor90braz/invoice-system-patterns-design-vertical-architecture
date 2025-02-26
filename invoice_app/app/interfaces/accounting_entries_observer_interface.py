from abc import ABC, abstractmethod
from invoice_app.models.invoice import Invoice

class BaseAccountingEntriesObserverInterface(ABC):
    @abstractmethod
    def update(self, invoice: Invoice):
        pass