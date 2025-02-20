from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_interface import BaseInvoiceAccountingEntriesInterface
from InvoiceSystem.models import Invoice


def get_accounting_strategy(invoice: Invoice) -> BaseInvoiceAccountingEntriesInterface:

    match invoice.invoice_type:
        case "purchase":
            return PurchaseStrategy()
        case "expense":
            return ExpenseStrategy()
        case "investment":
            return InvestmentStrategy()
        case _:
            raise ValueError(f"Unsupported invoice type: {invoice.invoice_type}")
