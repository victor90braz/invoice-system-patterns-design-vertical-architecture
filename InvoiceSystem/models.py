from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, EmailValidator
from django.db import models
from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    invoice_type = models.CharField(
        max_length=20,
        choices=InvoiceType.choices,  
        default=InvoiceType.PURCHASE_INVOICE,  
    )
    customer_name = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_email = models.EmailField(max_length=255)
    product_type = models.CharField(max_length=50, blank=True, null=True)  
    supplier_country = models.CharField(max_length=50, blank=True, null=True)  
    tax_regime = models.CharField(max_length=50, blank=True, null=True)  

    def clean(self):
        super().clean()

        if Invoice.objects.filter(invoice_number=self.invoice_number).exists():
            raise ValidationError({'invoice_number': 'Invoice number must be unique.'})

        if self.total_value <= 0:
            raise ValidationError({'total_value': 'Total value must be a positive number.'})

        if self.customer_email:
            email_validator = EmailValidator()
            try:
                email_validator(self.customer_email)
            except ValidationError:
                raise ValidationError({'customer_email': 'Invalid email address format.'})

        if self.product_type and self.invoice_type == 'PURCHASE_INVOICE' and self.product_type not in ['goods', 'services']:
            raise ValidationError({'product_type': 'Product type must be "goods" or "services" for purchase invoices.'})

        if not self.supplier_country and self.tax_regime:
            raise ValidationError({'supplier_country': 'Supplier country must be provided when tax regime is specified.'})
        if self.supplier_country and not self.tax_regime:
            raise ValidationError({'tax_regime': 'Tax regime must be provided when supplier country is specified.'})

        if self.product_type and self.invoice_type == 'PURCHASE_INVOICE' and self.product_type not in ['goods', 'services']:
            raise ValidationError({'product_type': 'Product type must be "goods" or "services" for purchase invoices.'})

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer_name}"
