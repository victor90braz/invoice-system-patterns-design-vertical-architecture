from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface

class TreasuryObserver(BaseAccountingEntriesObserverInterface):

    def update(self, invoice):
        print(f"Notifying treasury about invoice {invoice.invoice_number}")