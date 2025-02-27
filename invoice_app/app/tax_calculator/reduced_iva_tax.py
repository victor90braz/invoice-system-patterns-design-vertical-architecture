from invoice_app.app.tax_calculator.enums.tax_rate_enums import TaxRate
from invoice_app.app.tax_calculator.service.base_tax_rule import BaseTaxRule

class ReducedIVATax(BaseTaxRule):
    tax_rate = TaxRate.REDUCED_IVA.value
