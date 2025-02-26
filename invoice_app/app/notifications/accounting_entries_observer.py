from invoice_app.app.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface
from invoice_app.models.invoice import Invoice


class AccountingEntriesObserver(BaseAccountingEntriesObserverInterface):

    def update(self, invoice: Invoice):
        print(f"Updating accounting balances for invoice {invoice.invoice_number}")