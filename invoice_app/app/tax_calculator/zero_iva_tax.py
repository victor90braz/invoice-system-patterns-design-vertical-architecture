from decimal import Decimal
from invoice_app.app.interfaces.tax_rule_interface import TaxRuleInterface


class ZeroIVATax(TaxRuleInterface):
    def calculate_tax(self, amount: Decimal) -> Decimal:
        return Decimal("0.00")  # Exento de IVA