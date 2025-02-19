
from InvoiceSystem.invoices.states.base_invoice_state import BaseInvoiceState

class CancelledState(BaseInvoiceState):
    def approve(self, invoice):
        raise ValueError("No se puede aprobar una factura cancelada.")
    
    def cancel(self, invoice):
        raise ValueError("La factura ya está cancelada.")
    
    def pay(self, invoice):
        raise ValueError("No se puede pagar una factura cancelada.")
