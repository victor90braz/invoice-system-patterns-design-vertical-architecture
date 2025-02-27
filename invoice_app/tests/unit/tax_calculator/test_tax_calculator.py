from django.test import TestCase
from decimal import Decimal

from invoice_app.app.tax_calculator.tax_calculator import TaxCalculator
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.supplier_factory import SupplierFactory
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory


class TestTaxCalculator(TestCase):

    def test_calculate_total_tax_with_matching_policy(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create(rate=Decimal("21.00"), product_type="electronics", country="US")
        supplier = SupplierFactory.create(country="US")
        supplier.tax_policies.set([tax_policy])
        supplier.refresh_from_db()

        invoice = InvoiceFactory.create(
            total_value=Decimal("100.00"),
            invoice_type="electronics",
            supplier=supplier
        )

        # Act
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 1)
        self.assertEqual(total_tax, Decimal("21.00"))

    def test_calculate_total_tax_with_custom_tax_rate(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create(rate=Decimal("15.00"), product_type="software", country="DE")
        supplier = SupplierFactory.create(country="DE")
        supplier.tax_policies.set([tax_policy])
        supplier.refresh_from_db()

        invoice = InvoiceFactory.create(
            total_value=Decimal("100.00"),
            invoice_type="software",
            supplier=supplier
        )

        # Act
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 1)
        self.assertEqual(total_tax, Decimal("15.00"))

    def test_calculate_total_tax_no_matching_policy(self):
        # Arrange
        supplier = SupplierFactory.create()
        supplier.tax_policies.clear()

        invoice = InvoiceFactory.create(
            total_value=Decimal("150.00"),
            invoice_type="clothing",
            supplier=supplier
        )

        # Act
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 0)
        self.assertEqual(total_tax, Decimal("0.00"))

    def test_calculate_total_tax_with_zero_tax_policy(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create(rate=Decimal("0.00"), product_type="books", country="FR")
        supplier = SupplierFactory.create(country="FR")
        supplier.tax_policies.set([tax_policy])
        supplier.refresh_from_db()

        invoice = InvoiceFactory.create(
            total_value=Decimal("200.00"),
            invoice_type="books",
            supplier=supplier
        )

        # Act
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 1)
        self.assertEqual(total_tax, Decimal("0.00"))
