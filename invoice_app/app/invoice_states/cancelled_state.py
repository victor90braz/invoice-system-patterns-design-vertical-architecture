from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.models.invoice import Invoice  # Asegúrate de importar también el modelo Invoice

class CancelledState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        """No se puede aprobar una factura cancelada"""
        raise ValueError(f"Cannot approve an invoice in {self.__class__.__name__} state. The invoice is already cancelled.")

    def cancel(self, invoice: Invoice):
        """La factura ya está cancelada, no se puede cancelar de nuevo"""
        raise ValueError(f"Invoice {invoice.invoice_number} is already cancelled. No further cancellation is possible.")

    def pay(self, invoice: Invoice):
        """No se puede pagar una factura cancelada"""
        raise ValueError(f"Cannot pay an invoice in {self.__class__.__name__} state. The invoice is cancelled and cannot be paid.")

    def validate_transition(self, invoice: Invoice, target_state: str):
        """Validar transiciones desde 'cancelled'"""
        if target_state == 'approved':
            raise ValueError("Cancelled invoices cannot be re-approved.")
        # Agregar más reglas de transición si es necesario
