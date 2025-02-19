from InvoiceSystem.taxes.strategies.base_tax_strategy import BaseTaxStrategy


class CombinedTaxStrategy(BaseTaxStrategy):
    def __init__(self, strategies):
        self.strategies = strategies  # List of strategies

    def calculate_tax(self, invoice):
        # Adjust the tax calculation based on specific rules.
        if invoice.product_type == "food":
            # If the product type is food, only apply the reduced tax rate.
            return self.strategies[1].calculate_tax(invoice)  # Apply only the reduced tax

        # Otherwise, sum both taxes for other cases
        total_tax = 0
        for strategy in self.strategies:
            total_tax += strategy.calculate_tax(invoice)
        return total_tax
