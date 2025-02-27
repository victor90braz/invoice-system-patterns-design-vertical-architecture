from invoice_app.app.tax_calculator.enums.tax_rate_enums import TaxRate
from invoice_app.app.tax_calculator.rules.base_tax_rule import BaseTaxRule

class ZeroIVATax(BaseTaxRule):
    tax_rate = TaxRate.ZERO_IVA.value
