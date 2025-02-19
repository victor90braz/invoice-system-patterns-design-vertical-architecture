from InvoiceSystem.taxes.strategies.base_tax_strategy import BaseTaxStrategy


class StandardTaxStrategy(BaseTaxStrategy):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.21  # Example 21% tax rate for standard tax
