from abc import ABC, abstractmethod

class BaseInvoiceStateInterface(ABC):
    
    @abstractmethod
    def approve(self, invoice):
        """Approve the invoice if valid for approval"""
        pass

    @abstractmethod
    def cancel(self, invoice):
        """Cancel the invoice if valid for cancellation"""
        pass

    @abstractmethod
    def pay(self, invoice):
        """Pay the invoice if valid for payment"""
        pass

    @abstractmethod
    def validate_transition(self, invoice, target_state):
        """Validates if the transition to a given target state is allowed"""
        pass
