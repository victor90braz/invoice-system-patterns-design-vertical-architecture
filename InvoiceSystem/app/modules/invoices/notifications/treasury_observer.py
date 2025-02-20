from InvoiceSystem.app.modules.invoices.notifications.accounting_entries_observer import AccountingEntriesObserver


class TreasuryObserver(AccountingEntriesObserver):
    def update(self, invoice):
        print(f"Notificando a tesorería sobre la factura {invoice.invoice_number}")