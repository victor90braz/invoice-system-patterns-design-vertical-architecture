from django.test import TestCase
from decimal import Decimal
from invoice_app.app.tax_calculator.rules.reduced_iva_tax import ReducedIVATax
from invoice_app.app.tax_calculator.rules.standard_iva_tax import StandardIVATax
from invoice_app.app.tax_calculator.rules.zero_iva_tax import ZeroIVATax
from invoice_app.app.tax_calculator.tax_calculator import TaxCalculator
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory
from invoice_app.app.tax_calculator.composite_tax_rule import CompositeTaxRule


class TestCompositeTaxRule(TestCase):

    def test_apply_multiple_tax_rules(self):
        # Arrange
        amount = Decimal("100.00")
        standard_tax = StandardIVATax()
        reduced_tax = ReducedIVATax()
        zero_tax = ZeroIVATax()

        CompositeTaxRule.add_rule(standard_tax)
        CompositeTaxRule.add_rule(reduced_tax)
        CompositeTaxRule.add_rule(zero_tax)

        # Act
        total_tax = CompositeTaxRule.calculate_total_tax(amount)

        # Assert
        self.assertEqual(total_tax, Decimal("31.00"))

    def test_apply_standard_iva_tax(self):
        # Arrange
        policy = TaxPolicyFactory.create(rate=Decimal("21.00"))
        amount = Decimal("100.00")

        # Act
        tax = TaxCalculator.apply_tax_policy(policy, amount)

        # Assert
        self.assertEqual(tax, Decimal("21.00"))

    def test_apply_reduced_iva_tax(self):
        # Arrange
        policy = TaxPolicyFactory.create(rate=Decimal("10.00"))
        amount = Decimal("200.00")

        # Act
        tax = TaxCalculator.apply_tax_policy(policy, amount)

        # Assert
        self.assertEqual(tax, Decimal("20.00"))

    def test_apply_zero_iva_tax(self):
        # Arrange
        policy = TaxPolicyFactory.create(rate=Decimal("0.00"))
        amount = Decimal("150.00")

        # Act
        tax = TaxCalculator.apply_tax_policy(policy, amount)

        # Assert
        self.assertEqual(tax, Decimal("0.00"))

    def test_apply_custom_tax_rate(self):
        # Arrange
        policy = TaxPolicyFactory.create(rate=Decimal("15.00"))
        amount = Decimal("100.00")

        # Act
        tax = TaxCalculator.apply_tax_policy(policy, amount)

        # Assert
        self.assertEqual(tax, Decimal("15.00"))
