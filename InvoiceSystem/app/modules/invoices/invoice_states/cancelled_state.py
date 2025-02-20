from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface


class CancelledState(BaseInvoiceStateInterface):
    """Estado de una factura cancelada."""

    def approve(self, invoice):
        """Transición a estado aprobado."""
        print(f"No se puede aprobar una factura en estado {self}.")

    def cancel(self, invoice):
        """Transición a estado cancelado."""
        print(f"La factura {invoice.invoice_id} ya está cancelada (estado {self}).")

    def pay(self, invoice):
        """Transición a estado pagado."""
        print(f"No se puede pagar una factura en estado {self}.")