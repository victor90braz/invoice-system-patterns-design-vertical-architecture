from invoice_app.app.interfaces.accounting_entries_interface import BaseInvoiceAccountingEntriesInterface
from invoice_app.models.invoice import Invoice


class InvestmentStrategy(BaseInvoiceAccountingEntriesInterface):
    def generate_entry(self, invoice: Invoice) -> dict:
        return {
            "account": f"100 - {invoice.invoice_type}",
            "amount": invoice.total_value,
            "description": f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}"
        }
