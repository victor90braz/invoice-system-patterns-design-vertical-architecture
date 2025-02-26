from invoice_app.app.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface
from invoice_app.models.invoice import Invoice


class TreasuryObserver(BaseAccountingEntriesObserverInterface):

    def update(self, invoice: Invoice):
        print(f"Notifying treasury about invoice {invoice.invoice_number}")