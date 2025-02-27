from django.db import models


class TaxPolicy(models.Model):
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    product_type = models.CharField(max_length=100)  
    tax_regime = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.product_type} - {self.tax_regime}: {self.rate}%"
