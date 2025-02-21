from InvoiceSystem.app.modules.invoices.interfaces.tax_rule_interface import TaxRuleInterface
from InvoiceSystem.models import Invoice
from decimal import Decimal


class SupplierCountryTaxCalculator(TaxRuleInterface):

    def __init__(self, country: str, tax_rate: Decimal):
        self.country = country
        self.tax_rate = tax_rate

    def calculate_tax(self, invoice: Invoice) -> Decimal:
        if invoice.supplier_country == self.country:
            return invoice.total_value * self.tax_rate
        return Decimal('0.00')
