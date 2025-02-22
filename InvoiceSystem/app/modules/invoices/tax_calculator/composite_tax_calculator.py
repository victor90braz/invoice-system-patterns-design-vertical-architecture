from InvoiceSystem.app.modules.invoices.interfaces.tax_rule_interface import TaxRuleInterface
from InvoiceSystem.app.modules.invoices.models.invoice import Invoice
from decimal import Decimal


class CompositeTaxCalculator(TaxRuleInterface):

    def __init__(self):
        self.tax_calculators = []

    def add_tax_calculator(self, tax_calculator: TaxRuleInterface):
        self.tax_calculators.append(tax_calculator)

    def calculate_tax(self, invoice: Invoice) -> Decimal:
        total_tax = Decimal('0.00')
        for tax_calculator in self.tax_calculators:
            total_tax += tax_calculator.calculate_tax(invoice)
        return total_tax
