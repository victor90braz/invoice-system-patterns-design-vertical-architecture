from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_interface import BaseInvoiceAccountingEntriesInterface
from InvoiceSystem.app.modules.invoices.models.invoice import Invoice


class PurchaseStrategy(BaseInvoiceAccountingEntriesInterface):
    def generate_entry(self, invoice: Invoice) -> dict:
        return {
            "account": f"500 - {invoice.invoice_type}",
            "amount": invoice.total_value,
            "description": f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}"
        }
