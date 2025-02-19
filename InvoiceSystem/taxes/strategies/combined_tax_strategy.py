from .base_tax_strategy import BaseTaxStrategy

class CombinedTaxStrategy(BaseTaxStrategy):
    def __init__(self, strategies):
        self.strategies = strategies  # Lista de estrategias

    def calculate_tax(self, invoice):
        total_tax = 0
        for strategy in self.strategies:
            total_tax += strategy.calculate_tax(invoice)
        return total_tax
