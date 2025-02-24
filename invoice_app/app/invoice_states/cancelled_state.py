from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface

class CancelledState(BaseInvoiceStateInterface):
    
    def approve(self, invoice):
        raise ValueError(f"Cannot approve an invoice in {self.__class__.__name__} state. The invoice is already cancelled.")

    def cancel(self, invoice):
        raise ValueError(f"Invoice {invoice.invoice_id} is already cancelled. No further cancellation is possible.")

    def pay(self, invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. The invoice is cancelled and cannot be paid.")

    def validate_transition(self, invoice, target_state):
        if target_state == 'approved':
            raise ValueError("Cancelled invoices cannot be re-approved.")
        # Add more transition rules if needed
