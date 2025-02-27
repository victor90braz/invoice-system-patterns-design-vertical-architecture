from decimal import Decimal
from invoice_app.app.interfaces.tax_rule_interface import TaxRuleInterface


class CountrySpecificTax(TaxRuleInterface):
    def __init__(self, rate: Decimal):
        self.rate = rate

    def calculate_tax(self, amount: Decimal) -> Decimal:
        return amount * self.rate