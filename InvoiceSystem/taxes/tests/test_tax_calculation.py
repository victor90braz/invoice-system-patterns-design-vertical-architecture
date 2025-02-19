from django.test import TestCase
from InvoiceSystem.taxes.models.invoice import Invoice
from taxes.factories.tax_strategy_factory import TaxStrategyFactory

class TaxCalculationTest(TestCase):
    def test_standard_tax(self):
        invoice = Invoice(total_value=100, country="España", product_type="other", tax_regime="general")
        strategy = TaxStrategyFactory.get_strategy(invoice)
        self.assertEqual(strategy.calculate_tax(invoice), 21)  # 21% de IVA sobre 100

    def test_reduced_tax(self):
        invoice = Invoice(total_value=100, country="España", product_type="food", tax_regime="general")
        strategy = TaxStrategyFactory.get_strategy(invoice)
        self.assertEqual(strategy.calculate_tax(invoice), 10)  # 10% de IVA sobre 100

    def test_international_tax(self):
        invoice = Invoice(total_value=100, country="Francia", product_type="other", tax_regime="general")
        strategy = TaxStrategyFactory.get_strategy(invoice)
        self.assertEqual(strategy.calculate_tax(invoice), 0)  # IVA 0% para ventas internacionales

    def test_combined_tax(self):
        invoice = Invoice(total_value=100, country="España", product_type="food", tax_regime="simplified")
        strategy = TaxStrategyFactory.get_strategy(invoice)
        self.assertEqual(strategy.calculate_tax(invoice), 10)  # IVA reducido 10% + IVA estándar combinado
