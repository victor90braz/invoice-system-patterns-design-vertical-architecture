from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.models.invoice import Invoice  # Asegúrate de importar también el modelo Invoice

class DraftState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        """Transición de 'draft' a 'posted'"""
        self.validate_transition(invoice, 'approved')
        invoice.state = InvoiceState.objects.get(code='posted')  # Obtiene el estado 'posted'
        invoice.save()

    def cancel(self, invoice: Invoice):
        """Transición de 'draft' a 'cancelled'"""
        self.validate_transition(invoice, 'cancelled')
        invoice.state = InvoiceState.objects.get(code='cancelled')  # Obtiene el estado 'cancelled'
        invoice.save()

    def pay(self, invoice: Invoice):
        """No se puede pagar directamente desde 'draft'"""
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. It must be approved first.")

    def validate_transition(self, invoice: Invoice, target_state: str):
        """Validar las transiciones permitidas desde 'draft'"""
        if target_state == 'approved' and invoice.total_value <= 0:
            raise ValueError("Invoice must have a positive total value to be approved.")
        if target_state == 'cancelled' and invoice.total_value == 0:
            raise ValueError("Cancelled invoices must have no outstanding balance.")
