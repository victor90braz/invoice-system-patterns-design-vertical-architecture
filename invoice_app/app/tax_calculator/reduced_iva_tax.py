from decimal import Decimal
from invoice_app.app.interfaces.tax_rule_interface import TaxRuleInterface


class ReducedIVATax(TaxRuleInterface):
    def calculate_tax(self, amount: Decimal) -> Decimal:
        return amount * Decimal("0.10")  # 10% IVA reducido