from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface

class AccountingEntriesObserver(BaseAccountingEntriesObserverInterface):

    def update(self, invoice):
        print(f"Updating accounting balances for invoice {invoice.invoice_number}")