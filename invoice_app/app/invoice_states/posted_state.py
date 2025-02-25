from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.models.invoice import Invoice

class PostedState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        """No se puede aprobar una factura ya publicada"""
        raise ValueError(f"Invoice {invoice.invoice_number} is already approved. It cannot be re-approved.")

    def cancel(self, invoice: Invoice):
        """Transición de 'posted' a 'cancelled'"""
        invoice.state = InvoiceState.objects.get(code='cancelled')  # Cambiar a estado 'cancelled'
        invoice.save()

    def pay(self, invoice: Invoice):
        """Transición de 'posted' a 'paid'"""
        invoice.state = InvoiceState.objects.get(code='paid')  # Cambiar a estado 'paid'
        invoice.save()

    def validate_transition(self, invoice: Invoice, target_state: str):
        """Validar las transiciones permitidas desde 'posted'"""
        pass  # Aquí no es necesario agregar validaciones adicionales
