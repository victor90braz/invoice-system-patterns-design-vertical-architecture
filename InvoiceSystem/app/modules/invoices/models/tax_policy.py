from django.db import models
from django.core.validators import MinValueValidator


class TaxPolicy(models.Model):
    product_type = models.CharField(max_length=50)  
    country = models.CharField(max_length=50)  
    tax_regime = models.CharField(max_length=50)  
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)]) 

    class Meta:
        unique_together = ("product_type", "country", "tax_regime")  

    def calculate_tax(self, amount):
        return round(amount * (self.tax_rate / 100), 2)

    def __str__(self):
        return f"{self.product_type} - {self.country} ({self.tax_regime}): {self.tax_rate}%"
