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
        total_tax = sum(
            invoice.total_value * (policy.rate / Decimal("100.00"))
            for policy in applicable_policies
        )
        return total_tax
