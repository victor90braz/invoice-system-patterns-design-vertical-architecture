from django.test import TestCase
from decimal import Decimal

import factory
from invoice_app.app.tax_calculator.service.tax_calculator import TaxCalculator
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.supplier_factory import SupplierFactory
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory

class TestTaxCalculator(TestCase):
    def test_calculate_total_tax_with_matching_policy(self):
        tax_policy = TaxPolicyFactory.create(rate=Decimal("21.00"), product_type="electronics")

        supplier = SupplierFactory.create()
        supplier.tax_policies.set([tax_policy])

        invoice = InvoiceFactory.create(
            total_value=Decimal("100.00"),
            invoice_type="electronics",
            supplier=supplier
        )

        total_tax = TaxCalculator.calculate_total_tax(invoice)

        self.assertEqual(supplier.tax_policies.count(), 1)
        self.assertEqual(total_tax, Decimal("21.00"))

    def test_calculate_total_tax_with_multiple_policies(self):
        tax_policies = TaxPolicyFactory.create_batch(
            2, 
            rate=factory.Iterator([Decimal("21.00"), Decimal("10.00")]), 
            product_type="electronics", 
            tax_regime="freelancer"
        )

        supplier = SupplierFactory.create()
        supplier.tax_policies.set(tax_policies)

        invoice = InvoiceFactory.create(
            total_value=Decimal("200.00"),
            invoice_type="electronics",
            supplier=supplier
        )

        total_tax = TaxCalculator.calculate_total_tax(invoice)

        self.assertEqual(supplier.tax_policies.count(), 2)
        self.assertEqual(total_tax, Decimal("62.00"))

    def test_calculate_total_tax_no_matching_policy(self):
        supplier = SupplierFactory.create()
        supplier.tax_policies.clear()

        invoice = InvoiceFactory.create(
            total_value=Decimal("150.00"),
            invoice_type="clothing",
            supplier=supplier
        )

        total_tax = TaxCalculator.calculate_total_tax(invoice)

        self.assertEqual(supplier.tax_policies.count(), 0)
        self.assertEqual(total_tax, Decimal("0.00"))

    def test_calculate_total_tax_with_custom_tax_rate(self):
        tax_policy = TaxPolicyFactory.create(rate=Decimal("15.00"), product_type="software")

        supplier = SupplierFactory.create()
        supplier.tax_policies.set([tax_policy])

        invoice = InvoiceFactory.create(
            total_value=Decimal("100.00"),
            invoice_type="software",
            supplier=supplier
        )

        total_tax = TaxCalculator.calculate_total_tax(invoice)

        self.assertEqual(supplier.tax_policies.count(), 1)
        self.assertEqual(total_tax, Decimal("15.00"))  # 100 * 0.15 = 15

    def test_calculate_total_tax_with_zero_tax_policy(self):
        tax_policy = TaxPolicyFactory.create(rate=Decimal("0.00"), product_type="books")

        supplier = SupplierFactory.create()
        supplier.tax_policies.set([tax_policy])

        invoice = InvoiceFactory.create(
            total_value=Decimal("200.00"),
            invoice_type="books",
            supplier=supplier
        )

        total_tax = TaxCalculator.calculate_total_tax(invoice)

        self.assertEqual(supplier.tax_policies.count(), 1)
        self.assertEqual(total_tax, Decimal("0.00"))
