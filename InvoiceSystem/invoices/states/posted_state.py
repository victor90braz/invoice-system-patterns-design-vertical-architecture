from InvoiceSystem.invoices.states.base_invoice_state import BaseInvoiceState, CancelledState, PaidState

class PostedState(BaseInvoiceState):
    def approve(self, invoice):
        raise ValueError("La factura ya está aprobada.")
    
    def cancel(self, invoice):
        print("Factura cancelada desde estado contabilizado.")
        invoice.state = CancelledState()

    def pay(self, invoice):
        print("Factura pagada desde estado contabilizado.")
        invoice.state = PaidState()
