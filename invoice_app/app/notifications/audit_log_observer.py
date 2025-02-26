from invoice_app.app.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface
from invoice_app.models.invoice import Invoice


class AuditLogObserver(BaseAccountingEntriesObserverInterface):
    """Observer responsible for generating an audit log."""

    def update(self, invoice: Invoice):
        print(f"Generating audit log for invoice {invoice.invoice_number}")