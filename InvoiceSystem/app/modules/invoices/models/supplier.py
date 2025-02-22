from django.db import models
from InvoiceSystem.app.modules.invoices.models.tax_policy import TaxPolicy  

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tax_policy = models.ForeignKey(TaxPolicy, on_delete=models.SET_NULL, null=True, blank=True, related_name="suppliers")  

    def __str__(self):
        return self.name
