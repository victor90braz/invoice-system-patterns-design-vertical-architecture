from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_type = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    
    def __str__(self):
        return self.invoice_number
