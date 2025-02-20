from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from InvoiceSystem.models import Invoice  

class AccountingStrategyHelper:
    @staticmethod
    def get_strategy(invoice: Invoice):
        """
        Returns the appropriate accounting entry strategy based on the invoice type.

        :param invoice: The invoice object
        :return: The selected accounting entry strategy
        """
        match invoice.invoice_type:
            case "purchase":
                return PurchaseStrategy()
            case "expense":
                return ExpenseStrategy()
            case "investment":
                return InvestmentStrategy()
            case _:
                raise ValueError(f"Unsupported invoice type: {invoice.invoice_type}")
