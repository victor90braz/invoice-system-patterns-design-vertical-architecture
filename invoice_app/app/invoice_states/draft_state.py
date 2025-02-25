from invoice_app.models.invoice import Invoice
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.app.signals.signals import invoice_approved, invoice_cancelled  

class DraftState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        self.validate_transition(invoice, 'approved')
        invoice.state = InvoiceState.objects.get(code='posted')
        invoice.save()
        self._send_invoice_approved_signal(invoice)

    def cancel(self, invoice: Invoice):
        self.validate_transition(invoice, 'cancelled')
        invoice.state = InvoiceState.objects.get(code='cancelled')
        invoice.save()
        self._send_invoice_cancelled_signal(invoice)

    def pay(self, invoice: Invoice):
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. It must be approved first.")

    def validate_transition(self, invoice: Invoice, target_state: str):
        if target_state == 'approved' and invoice.total_value <= 0:
            raise ValueError("Invoice must have a positive total value to be approved.")
        if target_state == 'cancelled' and invoice.total_value != 0:
            raise ValueError("Cancelled invoices must have no outstanding balance.")

    def _send_invoice_approved_signal(self, invoice: Invoice):
        # Use the signal
        invoice_approved.send(sender=self.__class__, invoice=invoice)

    def _send_invoice_cancelled_signal(self, invoice: Invoice):
        # Use the signal
        invoice_cancelled.send(sender=self.__class__, invoice=invoice)