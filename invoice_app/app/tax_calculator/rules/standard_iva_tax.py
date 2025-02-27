from invoice_app.app.tax_calculator.enums.tax_rate_enums import TaxRate
from invoice_app.app.tax_calculator.rules.base_tax_rule import BaseTaxRule

class StandardIVATax(BaseTaxRule):
    tax_rate = TaxRate.STANDARD_IVA.value
