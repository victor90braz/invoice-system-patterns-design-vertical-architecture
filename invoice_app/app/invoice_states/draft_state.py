from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.app.invoice_states.cancelled_state import CancelledState
from invoice_app.app.invoice_states.posted_state import PostedState


class DraftState(BaseInvoiceStateInterface):

    def approve(self, invoice):
        invoice.state = PostedState()

    def cancel(self, invoice):
        invoice.state = CancelledState()

    def pay(self, invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. It must be approved first.")
