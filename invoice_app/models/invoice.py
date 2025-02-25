from django.db import models
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.app.accounting_entries.strategies.types.invoice_type import InvoiceType
from invoice_app.models.supplier import Supplier

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_type = models.CharField(max_length=50, choices=InvoiceType.choices)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    state = models.ForeignKey(InvoiceState, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.invoice_number
