from InvoiceSystem.invoices.states.base_invoice_state import BaseInvoiceState, CancelledState, PostedState

class DraftState(BaseInvoiceState):
    def approve(self, invoice):
        print("Factura aprobada desde estado borrador.")
        invoice.state = PostedState()

    def cancel(self, invoice):
        print("Factura cancelada desde estado borrador.")
        invoice.state = CancelledState()

    def pay(self, invoice):
        raise ValueError("No se puede pagar una factura en estado borrador.")
