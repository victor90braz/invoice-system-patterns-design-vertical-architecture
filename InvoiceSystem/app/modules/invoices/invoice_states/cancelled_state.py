from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface

class CancelledState(BaseInvoiceStateInterface):
    
    def approve(self, invoice):
        raise ValueError(f"Cannot approve an invoice in {self.__class__.__name__} state.")

    def cancel(self, invoice):
        raise ValueError(f"Invoice {invoice.invoice_id} is already cancelled.")

    def pay(self, invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state.")
