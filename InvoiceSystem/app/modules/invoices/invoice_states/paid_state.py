from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface

class PaidState(BaseInvoiceStateInterface):
    
    def approve(self, invoice):
        raise ValueError(f"Invoice {invoice.invoice_id} is already paid.")

    def cancel(self, invoice):
        raise ValueError(f"Cannot cancel an invoice in {self.__class__.__name__} state.")

    def pay(self, invoice):
        raise ValueError(f"Invoice {invoice.invoice_id} is already paid.")
