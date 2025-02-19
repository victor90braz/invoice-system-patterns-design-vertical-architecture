from InvoiceSystem.taxes.strategies.base_tax_strategy import BaseTaxStrategy


class ReducedTaxStrategy(BaseTaxStrategy):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.10  # Example 10% tax rate for reduced tax
