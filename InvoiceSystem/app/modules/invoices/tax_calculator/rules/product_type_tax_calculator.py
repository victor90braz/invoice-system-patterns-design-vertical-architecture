from InvoiceSystem.app.modules.invoices.interfaces.tax_rule_interface import TaxRuleInterface
from InvoiceSystem.models import Invoice
from decimal import Decimal


class ProductTypeTaxCalculator(TaxRuleInterface):

    def __init__(self, product_type: str, tax_rate: Decimal):
        self.product_type = product_type
        self.tax_rate = tax_rate

    def calculate_tax(self, invoice: Invoice) -> Decimal:
        if invoice.product_type == self.product_type:
            return invoice.total_value * self.tax_rate
        return Decimal('0.00')
