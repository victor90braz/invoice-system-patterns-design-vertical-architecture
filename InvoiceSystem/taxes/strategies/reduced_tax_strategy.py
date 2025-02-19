from .base_tax_strategy import BaseTaxStrategy

class ReducedTaxStrategy(BaseTaxStrategy):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.10  # IVA reducido del 10% (Ej. alimentos, medicamentos)
