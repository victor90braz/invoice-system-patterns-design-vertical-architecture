from django.db import models

class InvoiceState(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    description = models.TextField()
    is_final = models.BooleanField(default=False)

    def __str__(self):
        return self.name
