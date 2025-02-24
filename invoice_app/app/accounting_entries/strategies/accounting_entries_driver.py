from invoice_app.app.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from invoice_app.app.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from invoice_app.app.accounting_entries.strategies.types.invoice_type import InvoiceType
from invoice_app.app.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from invoice_app.models.invoice import Invoice


STRATEGY_MAP = {
    InvoiceType.PURCHASE_INVOICE: PurchaseStrategy,
    InvoiceType.EXPENSE_INVOICE: ExpenseStrategy,
    InvoiceType.INVESTMENT_INVOICE: InvestmentStrategy
}

class AccountingEntriesDriver:
    @staticmethod
    def get_strategy(invoice: Invoice):
        strategy_class = STRATEGY_MAP.get(invoice.invoice_type)
        if not strategy_class:
            raise ValueError(f"Unsupported invoice type: {invoice.invoice_type}")
        return strategy_class()
