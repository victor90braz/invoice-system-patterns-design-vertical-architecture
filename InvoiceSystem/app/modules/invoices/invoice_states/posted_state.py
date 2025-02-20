from InvoiceSystem.app.modules.invoices.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from InvoiceSystem.app.modules.invoices.invoice_states.cancelled_state import CancelledState
from InvoiceSystem.app.modules.invoices.invoice_states.paid_state import PaidState


class PostedState(BaseInvoiceStateInterface):
    """Estado de una factura aprobada (contabilizada)."""

    def approve(self, invoice):
        """Transición a estado aprobado."""
        print(f"La factura {invoice.invoice_id} ya está aprobada (estado {self}).")

    def cancel(self, invoice):
        """Transición a estado cancelado."""
        print(f"Factura {invoice.invoice_id} cancelada desde estado {self}.")
        invoice.state = CancelledState()  # Cambiar al estado "Cancelled"

    def pay(self, invoice):
        """Transición a estado pagado."""
        print(f"Factura {invoice.invoice_id} pagada desde estado {self}.")
        invoice.state = PaidState()  # Cambiar al estado "Paid"