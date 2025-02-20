from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface

class AccountingEntriesObserver(BaseAccountingEntriesObserverInterface):
    def update(self, invoice):
        print(f"Actualizando saldos contables para la factura {invoice.invoice_number}")
