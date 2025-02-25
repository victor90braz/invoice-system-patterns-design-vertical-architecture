from django.db import models

class InvoiceState(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
