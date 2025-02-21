from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from InvoiceSystem.app.modules.invoices.invoice_states.cancelled_state import CancelledState
from InvoiceSystem.app.modules.invoices.invoice_states.posted_state import PostedState

class DraftState(BaseInvoiceStateInterface):

    def approve(self, invoice):
        invoice.state = PostedState()

    def cancel(self, invoice):
        invoice.state = CancelledState()

    def pay(self, invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. It must be approved first.")
