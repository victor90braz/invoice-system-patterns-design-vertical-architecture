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
            return CombinedTaxStrategy()  # Combinación de IVA estándar y reducido
        return StandardTaxStrategy()  # IVA estándar por defecto
