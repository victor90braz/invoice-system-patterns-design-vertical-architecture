from django.test import TestCase
from decimal import Decimal
from invoice_app.app.tax_calculator.reduced_iva_tax import ReducedIVATax
from invoice_app.app.tax_calculator.service.tax_calculator import TaxCalculator
from invoice_app.app.tax_calculator.standard_iva_tax import StandardIVATax
from invoice_app.app.tax_calculator.zero_iva_tax import ZeroIVATax
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory


class TestApplyTaxPolicy(TestCase):
    def test_apply_standard_iva_tax(self):
        policy = TaxPolicyFactory.create(rate=Decimal("21.00"))
        amount = Decimal("100.00")

        tax = TaxCalculator.apply_tax_policy(policy, amount)

        self.assertIsInstance(StandardIVATax(), StandardIVATax)
        self.assertEqual(tax, Decimal("21.00"))  # 100 * 0.21

    def test_apply_reduced_iva_tax(self):
        policy = TaxPolicyFactory.create(rate=Decimal("10.00"))
        amount = Decimal("200.00")

        tax = TaxCalculator.apply_tax_policy(policy, amount)

        self.assertIsInstance(ReducedIVATax(), ReducedIVATax)
        self.assertEqual(tax, Decimal("20.00"))  # 200 * 0.10

    def test_apply_zero_iva_tax(self):
        policy = TaxPolicyFactory.create(rate=Decimal("0.00"))
        amount = Decimal("150.00")

        tax = TaxCalculator.apply_tax_policy(policy, amount)

        self.assertIsInstance(ZeroIVATax(), ZeroIVATax)
        self.assertEqual(tax, Decimal("0.00"))  # 150 * 0

    def test_apply_custom_tax_rate(self):
        policy = TaxPolicyFactory.create(rate=Decimal("15.00"))
        amount = Decimal("100.00")

        tax = TaxCalculator.apply_tax_policy(policy, amount)

        self.assertEqual(tax, Decimal("15.00"))  # 100 * 0.15
