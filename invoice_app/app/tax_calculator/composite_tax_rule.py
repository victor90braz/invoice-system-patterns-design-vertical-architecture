from decimal import Decimal
from typing import List
from invoice_app.app.interfaces.tax_rule_interface import TaxRuleInterface

class CompositeTaxRule:
    rules: List[TaxRuleInterface] = []

    @classmethod
    def add_rule(cls, rule: TaxRuleInterface) -> None:
        cls.rules.append(rule)

    @classmethod
    def calculate_total_tax(cls, amount: Decimal) -> Decimal:
        total_tax = Decimal("0.00")
        for rule in cls.rules:
            total_tax += rule.calculate_tax(amount)
        return total_tax
