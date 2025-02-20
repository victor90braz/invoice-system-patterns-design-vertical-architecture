from InvoiceSystem.app.modules.invoices.interfaces.invoice_tax_calculator_interface import BaseInvoiceTaxCalculatorInterface


class CombinedTaxStrategy(BaseInvoiceTaxCalculatorInterface):
    def __init__(self, strategies):
        self.strategies = strategies  # List of strategies

    def calculate_tax(self, invoice):
        # Apply the combined tax logic based on the product type and invoice data
        if invoice.product_type == "food":
            return self.calculate_reduced_tax(invoice)

        return self.calculate_combined_tax(invoice)

    def calculate_reduced_tax(self, invoice):
        # Apply only the reduced tax strategy
        return self.strategies[1].calculate_tax(invoice)  # Assuming reduced tax is the second strategy

    def calculate_combined_tax(self, invoice):
        # Apply the combined tax of both strategies
        total_tax = 0
        for strategy in self.strategies:
            total_tax += strategy.calculate_tax(invoice)
        return total_tax
