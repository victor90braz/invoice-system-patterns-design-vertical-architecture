from InvoiceSystem.app.modules.invoices.notifications.accounting_entries_observer import AccountingEntriesObserver


class AuditLogObserver(AccountingEntriesObserver):
    def update(self, invoice):
        print(f"Generando log de auditoría para la factura {invoice.invoice_number}")