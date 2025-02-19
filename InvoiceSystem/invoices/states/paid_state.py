
from InvoiceSystem.invoices.states.base_invoice_state import BaseInvoiceState

class PaidState(BaseInvoiceState):
    def approve(self, invoice):
        raise ValueError("La factura ya está pagada.")
    
    def cancel(self, invoice):
        raise ValueError("No se puede cancelar una factura ya pagada.")
    
    def pay(self, invoice):
        raise ValueError("La factura ya está pagada.")
