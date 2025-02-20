from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType
from InvoiceSystem.models import Invoice

class AccountingEntriesDriver:

    @staticmethod
    def get_strategy(invoice: Invoice):

        match invoice.invoice_type:
            case InvoiceType.PURCHASE:
                return PurchaseStrategy()
            case InvoiceType.EXPENSE:
                return ExpenseStrategy()
            case InvoiceType.INVESTMENT:
                return InvestmentStrategy()
            case _:
                raise ValueError(f"Unsupported invoice type: {invoice.invoice_type}")
