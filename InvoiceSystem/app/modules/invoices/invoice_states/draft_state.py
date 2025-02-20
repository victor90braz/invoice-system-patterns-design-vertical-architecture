from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface, CancelledState, PostedState


class DraftState(BaseInvoiceStateInterface):
    """Estado inicial de una factura (borrador)."""

    def approve(self, invoice):
        """Transición a estado aprobado."""
        print(f"Factura {invoice.invoice_id} aprobada desde estado {self}.")
        invoice.state = PostedState()  # Cambiar al estado "Posted"

    def cancel(self, invoice):
        """Transición a estado cancelado."""
        print(f"Factura {invoice.invoice_id} cancelada desde estado {self}.")
        invoice.state = CancelledState()  # Cambiar al estado "Cancelled"

    def pay(self, invoice):
        """Transición a estado pagado."""
        print(f"No se puede pagar una factura en estado {self}. Primero debe ser aprobada.")