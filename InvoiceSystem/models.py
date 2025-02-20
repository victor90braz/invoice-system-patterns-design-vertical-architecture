from django.db import models

from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_type = models.CharField(
        max_length=20,
        choices=InvoiceType.choices,  
        default=InvoiceType.PURCHASE_INVOICE,  
    )
    customer_name = models.CharField(max_length=255)
    customer_id = models.IntegerField()
