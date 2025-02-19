from InvoiceSystem.taxes.strategies.combined_tax_strategy import CombinedTaxStrategy
from InvoiceSystem.taxes.strategies.international_tax_strategy import InternationalTaxStrategy
from InvoiceSystem.taxes.strategies.reduced_tax_strategy import ReducedTaxStrategy
from InvoiceSystem.taxes.strategies.standard_tax_strategy import StandardTaxStrategy

class TaxStrategyFactory:
    @staticmethod
    def get_strategy(invoice):
        if invoice.country != "España":
            return InternationalTaxStrategy()  # No hay IVA para ventas internacionales
        if invoice.product_type == "food" and invoice.tax_regime == "general":
            return ReducedTaxStrategy()  # IVA reducido para alimentos
        if invoice.tax_regime == "simplified":
            # Crear la lista de estrategias para CombinedTaxStrategy
            standard_tax_strategy = StandardTaxStrategy()
            reduced_tax_strategy = ReducedTaxStrategy()
            return CombinedTaxStrategy([standard_tax_strategy, reduced_tax_strategy])  # Pasar la lista de estrategias
        return StandardTaxStrategy()  # IVA estándar por defecto
