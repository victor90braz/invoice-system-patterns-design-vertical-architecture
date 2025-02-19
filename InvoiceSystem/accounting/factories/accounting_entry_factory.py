from InvoiceSystem.accounting.strategies.airbnb_purchase_strategy import AirbnbExpenseStrategy
from InvoiceSystem.accounting.strategies.investment_purchase_strategy import InvestmentStrategy
from InvoiceSystem.accounting.strategies.mercadona_purchase_strategy import MercadonaPurchaseStrategy

# accounting/factories/accounting_entry_factory.py
class AccountingEntryFactory:
    @staticmethod
    def get_strategy(invoice_type):
        strategies = {
            "mercadona_purchase": MercadonaPurchaseStrategy(),
            "airbnb_expense": AirbnbExpenseStrategy(),
            "investment": InvestmentStrategy(),
        }

        if invoice_type not in strategies:
            raise ValueError(f"Estrategia no definida para el tipo: {invoice_type}")

        return strategies[invoice_type]
