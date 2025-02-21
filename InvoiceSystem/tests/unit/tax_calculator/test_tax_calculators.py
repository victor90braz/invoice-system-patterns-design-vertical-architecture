from decimal import Decimal
from django.test import TestCase

from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType
from InvoiceSystem.app.modules.invoices.tax_calculator.composite_tax_calculator import CompositeTaxCalculator
from InvoiceSystem.app.modules.invoices.tax_calculator.rules.product_type_tax_calculator import ProductTypeTaxCalculator
from InvoiceSystem.app.modules.invoices.tax_calculator.rules.supplier_country_tax_calculator import SupplierCountryTaxCalculator
from InvoiceSystem.app.modules.invoices.tax_calculator.rules.tax_regime_tax_calculator import TaxRegimeTaxCalculator
from InvoiceSystem.database.factories.invoice_factory import InvoiceFactory


class TaxCalculatorTestCase(TestCase):

    def setUp(self):
        self.invoice = InvoiceFactory(
            invoice_type=InvoiceType.PURCHASE_INVOICE,
            total_value=Decimal("100.00"),
            customer_name="Carlos García",
            customer_id=1,
            customer_email="carlos.garcia@example.com",
        )

    def test_product_type_tax_calculator(self):
        # Arrange
        self.invoice.product_type = "electronics"
        self.invoice.save()

        # Act
        tax_calculator = ProductTypeTaxCalculator(product_type="electronics", tax_rate=Decimal("0.10"))
        tax = tax_calculator.calculate_tax(self.invoice)

        # Assert
        self.assertEqual(tax, Decimal("10.00"))

    def test_supplier_country_tax_calculator(self):
        # Arrange
        self.invoice.supplier_country = "Germany"
        self.invoice.save()

        # Act
        tax_calculator = SupplierCountryTaxCalculator(country="Germany", tax_rate=Decimal("0.19"))
        tax = tax_calculator.calculate_tax(self.invoice)

        # Assert
        self.assertEqual(tax, Decimal("19.00"))

    def test_tax_regime_tax_calculator(self):
        # Arrange
        self.invoice.tax_regime = "VAT"
        self.invoice.save()

        # Act
        tax_calculator = TaxRegimeTaxCalculator(tax_regime="VAT", tax_rate=Decimal("0.15"))
        tax = tax_calculator.calculate_tax(self.invoice)

        # Assert
        self.assertEqual(tax, Decimal("15.00"))

    def test_composite_tax_calculator(self):
        # Arrange
        self.invoice.product_type = "electronics"
        self.invoice.supplier_country = "Germany"
        self.invoice.tax_regime = "VAT"
        self.invoice.save()

        composite_calculator = CompositeTaxCalculator()
        composite_calculator.add_tax_calculator(ProductTypeTaxCalculator(product_type="electronics", tax_rate=Decimal("0.10")))
        composite_calculator.add_tax_calculator(SupplierCountryTaxCalculator(country="Germany", tax_rate=Decimal("0.19")))
        composite_calculator.add_tax_calculator(TaxRegimeTaxCalculator(tax_regime="VAT", tax_rate=Decimal("0.15")))

        # Act
        total_tax = composite_calculator.calculate_tax(self.invoice)

        # Assert
        self.assertEqual(total_tax, Decimal("44.00"))
