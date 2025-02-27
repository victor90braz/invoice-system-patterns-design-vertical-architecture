from django.db import models
from invoice_app.models.tax_policy import TaxPolicy

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)    
    country = models.CharField(max_length=3, null=True, blank=True)  
    tax_policies = models.ManyToManyField(TaxPolicy, blank=True) 

    def __str__(self):
        return self.name
