from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum
from invoice_app.models.invoice import Invoice
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.app.signals.signals import invoice_cancelled

class PostedState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        raise ValueError(f"Invoice {invoice.invoice_number} is already posted. It cannot be approved again.")

    def cancel(self, invoice: Invoice):
        self.validate_transition(invoice, InvoiceStateEnum.CANCELLED)
        invoice.state = InvoiceState.objects.get(code=InvoiceStateEnum.CANCELLED)
        invoice.save()
        self._send_invoice_cancelled_signal(invoice)

    def pay(self, invoice: Invoice):
        self.validate_transition(invoice, InvoiceStateEnum.PAID)
        invoice.state = InvoiceState.objects.get(code=InvoiceStateEnum.PAID)
        invoice.save()

    def validate_transition(self, invoice: Invoice, target_state: str):
        if target_state == InvoiceStateEnum.PAID and invoice.total_value <= 0:
            raise ValueError("Invoice must have a positive total value to be paid.")
        if target_state == InvoiceStateEnum.CANCELLED and invoice.total_value != 0:
            raise ValueError("Cancelled invoices must have no outstanding balance.")

    def _send_invoice_cancelled_signal(self, invoice: Invoice):
        invoice_cancelled.send(sender=self.__class__, invoice=invoice)
