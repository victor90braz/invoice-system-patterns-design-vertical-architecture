from decimal import Decimal
from invoice_app.app.tax_calculator.enums.tax_constants import TaxConstants
from invoice_app.app.tax_calculator.enums.tax_rate_enums import TaxRate
from invoice_app.app.interfaces.tax_rule_interface import TaxRuleInterface

class StandardIVATax(TaxRuleInterface):
    def calculate_tax(self, amount: Decimal) -> Decimal:
        return amount * (Decimal(TaxRate.STANDARD_IVA.value) / Decimal(TaxConstants.PERCENTAGE_DIVISOR.value))
