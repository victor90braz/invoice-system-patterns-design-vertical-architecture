from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface


class PaidState(BaseInvoiceStateInterface):
    """Estado de una factura pagada."""

    def approve(self, invoice):
        """Transición a estado aprobado."""
        print(f"La factura {invoice.invoice_id} ya está pagada (estado {self}).")

    def cancel(self, invoice):
        """Transición a estado cancelado."""
        print(f"No se puede cancelar una factura en estado {self}.")

    def pay(self, invoice):
        """Transición a estado pagado."""
        print(f"La factura {invoice.invoice_id} ya está pagada (estado {self}).")