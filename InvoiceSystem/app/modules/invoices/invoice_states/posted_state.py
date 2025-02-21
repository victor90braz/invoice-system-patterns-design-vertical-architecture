from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from InvoiceSystem.app.modules.invoices.invoice_states.cancelled_state import CancelledState
from InvoiceSystem.app.modules.invoices.invoice_states.paid_state import PaidState

class PostedState(BaseInvoiceStateInterface):

    def approve(self, invoice):
        raise ValueError(f"Invoice {invoice.invoice_id} is already approved.")

    def cancel(self, invoice):
        invoice.state = CancelledState()

    def pay(self, invoice):
        invoice.state = PaidState()
