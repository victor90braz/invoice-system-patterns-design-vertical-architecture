from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.models.invoice import Invoice

class PaidState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        """No se puede aprobar una factura ya pagada"""
        raise ValueError(f"Invoice {invoice.invoice_number} is already paid. It cannot be approved.")

    def cancel(self, invoice: Invoice):
        """No se puede cancelar una factura ya pagada"""
        raise ValueError(f"Invoice {invoice.invoice_number} cannot be cancelled because it is already paid.")

    def pay(self, invoice: Invoice):
        """La factura ya está pagada"""
        raise ValueError(f"Invoice {invoice.invoice_number} is already paid.")

    def validate_transition(self, invoice: Invoice, target_state: str):
        """Validar las transiciones permitidas desde 'paid'"""
        pass  # No hace falta validación aquí
