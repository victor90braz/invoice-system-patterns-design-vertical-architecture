from invoice_app.app.tax_calculator.reduced_iva_tax import ReducedIVATax
from invoice_app.app.tax_calculator.standard_iva_tax import StandardIVATax
from invoice_app.app.tax_calculator.zero_iva_tax import ZeroIVATax
from invoice_app.models.invoice import Invoice
from invoice_app.models.tax_policy import TaxPolicy
from decimal import Decimal
from django.db import models


class TaxCalculator:
    @staticmethod
    def get_applicable_policies(invoice: Invoice):
        return TaxPolicy.objects.filter(
            supplier=invoice.supplier
        ).filter(
            models.Q(product_type=invoice.invoice_type) |
            models.Q(tax_regime__in=invoice.supplier.tax_policies.values_list("tax_regime", flat=True))
        )

    @staticmethod
    def calculate_total_tax(invoice: Invoice):
        applicable_policies = TaxCalculator.get_applicable_policies(invoice)
        total_tax = Decimal("0.00")

        for policy in applicable_policies:
            total_tax += TaxCalculator.apply_tax_policy(policy, invoice.total_value)

        return total_tax

    @staticmethod
    def apply_tax_policy(policy: TaxPolicy, amount: Decimal) -> Decimal:
        if policy.rate == Decimal("21.00"):
            return StandardIVATax().calculate_tax(amount)
        elif policy.rate == Decimal("10.00"):
            return ReducedIVATax().calculate_tax(amount)
        elif policy.rate == Decimal("0.00"):
            return ZeroIVATax().calculate_tax(amount)
        else:
            return amount * (policy.rate / Decimal("100.00"))
