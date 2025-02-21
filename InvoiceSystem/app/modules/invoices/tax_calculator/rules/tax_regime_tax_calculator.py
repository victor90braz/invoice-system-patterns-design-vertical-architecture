from InvoiceSystem.app.modules.invoices.interfaces.tax_rule_interface import TaxRuleInterface
from InvoiceSystem.models import Invoice
from decimal import Decimal


class TaxRegimeTaxCalculator(TaxRuleInterface):

    def __init__(self, tax_regime: str, tax_rate: Decimal):
        self.tax_regime = tax_regime
        self.tax_rate = tax_rate

    def calculate_tax(self, invoice: Invoice) -> Decimal:
        if invoice.tax_regime == self.tax_regime:
            return invoice.total_value * self.tax_rate
        return Decimal('0.00')
