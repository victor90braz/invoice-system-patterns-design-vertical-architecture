from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.app.invoice_states.cancelled_state import CancelledState
from invoice_app.app.invoice_states.posted_state import PostedState

class DraftState(BaseInvoiceStateInterface):

    def approve(self, invoice):
        # Validate transition and apply state change
        self.validate_transition(invoice, 'approved')
        invoice.state = PostedState()  # Transition to PostedState when approved
        invoice.save()

    def cancel(self, invoice):
        # Validate transition and apply state change
        self.validate_transition(invoice, 'cancelled')
        invoice.state = CancelledState()  # Transition to CancelledState
        invoice.save()

    def pay(self, invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. It must be approved first.")

    def validate_transition(self, invoice, target_state):
        if target_state == 'approved' and invoice.total_value <= 0:
            raise ValueError("Invoice must have a positive total value to be approved.")
        if target_state == 'cancelled' and invoice.total_value == 0:
            raise ValueError("Cancelled invoices must have no outstanding balance.")
