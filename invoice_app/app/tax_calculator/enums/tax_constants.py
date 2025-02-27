from django.db import models
from decimal import Decimal

class TaxConstants(models.TextChoices):
    PERCENTAGE_DIVISOR = str(Decimal("100")), "Percentage divisor (100%)"
