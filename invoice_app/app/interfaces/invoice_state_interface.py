from abc import ABC, abstractmethod

class BaseInvoiceStateInterface(ABC):
    
    @abstractmethod
    def approve(self, invoice):
        pass

    @abstractmethod
    def cancel(self, invoice):
        pass

    @abstractmethod
    def pay(self, invoice):
        pass
