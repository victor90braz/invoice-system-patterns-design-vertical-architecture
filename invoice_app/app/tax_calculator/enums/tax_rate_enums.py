from django.db import models
from decimal import Decimal

class TaxRate(models.TextChoices):
    STANDARD_IVA = str(Decimal("21.00")), "Standard IVA (21%)"
    REDUCED_IVA = str(Decimal("10.00")), "Reduced IVA (10%)"
    ZERO_IVA = str(Decimal("0.00")), "Zero IVA (0%)"
