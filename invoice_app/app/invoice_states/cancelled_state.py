from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.models.invoice import Invoice
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum

class CancelledState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        raise ValueError(f"Cannot approve an invoice in {self.__class__.__name__} state. The invoice is already cancelled.")

    def cancel(self, invoice: Invoice):
        raise ValueError(f"Invoice {invoice.invoice_number} is already cancelled. No further cancellation is possible.")

    def pay(self, invoice: Invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. The invoice is cancelled and cannot be paid.")

    def validate_transition(self, invoice: Invoice, target_state: str):
        if target_state == InvoiceStateEnum.APPROVED:
            raise ValueError("Cancelled invoices cannot be re-approved.")
