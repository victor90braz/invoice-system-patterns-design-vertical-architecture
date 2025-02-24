from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface

class PaidState(BaseInvoiceStateInterface):

    def approve(self, invoice):
        raise ValueError(f"Invoice {invoice.id} is already paid. It cannot be approved.")

    def cancel(self, invoice):
        raise ValueError(f"Invoice {invoice.id} cannot be cancelled because it is already paid.")

    def pay(self, invoice):
        raise ValueError(f"Invoice {invoice.invoice_id} is already paid. It cannot be paid again.")

    def validate_transition(self, invoice, target_state):
        if target_state == 'approved':
            raise ValueError("Paid invoices cannot be re-approved.")
        if target_state == 'cancelled':
            raise ValueError("Paid invoices cannot be cancelled.")
