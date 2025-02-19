from .base_tax_strategy import BaseTaxStrategy

class InternationalTaxStrategy(BaseTaxStrategy):
    def calculate_tax(self, invoice):
        return 0  # IVA 0% para ventas internacionales
