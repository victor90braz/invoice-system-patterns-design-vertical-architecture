from .base_tax_strategy import BaseTaxStrategy

class StandardTaxStrategy(BaseTaxStrategy):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.21  # IVA estándar del 21% en España
