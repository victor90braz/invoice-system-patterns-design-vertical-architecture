from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface

class AuditLogObserver(BaseAccountingEntriesObserverInterface):
    """Observer responsible for generating an audit log."""

    def update(self, invoice):
        print(f"Generating audit log for invoice {invoice.invoice_number}")