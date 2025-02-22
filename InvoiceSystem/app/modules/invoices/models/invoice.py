from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.invoice_type import InvoiceType
from InvoiceSystem.app.modules.invoices.models.supplier import Supplier


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    invoice_type = models.CharField(
        max_length=20,
        choices=InvoiceType.choices,
        default=InvoiceType.PURCHASE_INVOICE,
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="invoices")

    def clean(self):
        super().clean()
        if Invoice.objects.exclude(id=self.id).filter(invoice_number=self.invoice_number).exists():
            raise ValidationError({'invoice_number': 'Invoice number must be unique.'})

    def __str__(self):
        return f"Invoice {self.invoice_number} (Total: {self.total_value})"
