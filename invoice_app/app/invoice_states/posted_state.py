from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface

class PostedState(BaseInvoiceStateInterface):
    
    def approve(self, invoice):
        raise ValueError(f"Invoice {invoice.id} is already approved. It cannot be re-approved.")

    def cancel(self, invoice):
        raise ValueError(f"Invoice {invoice.id} cannot be cancelled because it is already posted.")

    
    def pay(self, invoice):
        invoice.state = 'paid'
        invoice.save()

    def validate_transition(self, invoice, target_state):
        if target_state == 'cancelled':
            raise ValueError("Posted invoices cannot be cancelled.")
