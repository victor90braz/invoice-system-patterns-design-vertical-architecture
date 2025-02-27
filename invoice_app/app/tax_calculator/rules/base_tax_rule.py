from decimal import Decimal
from invoice_app.app.interfaces.tax_rule_interface import TaxRuleInterface
from invoice_app.app.tax_calculator.enums.tax_constants import TaxConstants
from invoice_app.app.tax_calculator.enums.tax_rate_enums import TaxRate

class BaseTaxRule(TaxRuleInterface):
    tax_rate: TaxRate  

    @classmethod
    def calculate_tax(cls, amount: Decimal) -> Decimal:
        return amount * (Decimal(cls.tax_rate) / Decimal(TaxConstants.PERCENTAGE_DIVISOR.value))
