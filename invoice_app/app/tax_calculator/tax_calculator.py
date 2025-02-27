from invoice_app.app.tax_calculator.enums.tax_constants import TaxConstants
from invoice_app.app.tax_calculator.enums.tax_rate_enums import TaxRate
from invoice_app.app.tax_calculator.rules.reduced_iva_tax import ReducedIVATax
from invoice_app.app.tax_calculator.rules.standard_iva_tax import StandardIVATax
from invoice_app.app.tax_calculator.rules.zero_iva_tax import ZeroIVATax
from invoice_app.models.invoice import Invoice
from invoice_app.models.tax_policy import TaxPolicy
from decimal import Decimal
from django.db import models


class TaxCalculator:

    @staticmethod
    def calculate_total_tax(invoice: Invoice):
        applicable_policies = TaxCalculator.get_applicable_policies(invoice)
        return sum(TaxCalculator.apply_tax_policy(policy, invoice.total_value) for policy in applicable_policies)
    

    @staticmethod
    def get_applicable_policies(invoice: Invoice):
        return TaxPolicy.objects.filter(
            supplier=invoice.supplier,
            product_type=invoice.invoice_type
        ).filter(
            models.Q(country=invoice.supplier.country) | models.Q(country__isnull=True)
        )


    @staticmethod
    def apply_tax_policy(policy: TaxPolicy, amount: Decimal) -> Decimal:
        match str(policy.rate):
            case TaxRate.STANDARD_IVA.value:
                return StandardIVATax().calculate_tax(amount)
            case TaxRate.REDUCED_IVA.value:
                return ReducedIVATax().calculate_tax(amount)
            case TaxRate.ZERO_IVA.value:
                return ZeroIVATax().calculate_tax(amount)
            case _:
                return amount * (Decimal(policy.rate) / Decimal(TaxConstants.PERCENTAGE_DIVISOR.value))
