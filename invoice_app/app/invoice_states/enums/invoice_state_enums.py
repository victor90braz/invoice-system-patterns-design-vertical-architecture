from django.db import models

class InvoiceStateEnum(models.TextChoices):
    DRAFT = "Draft", "Draft"
    POSTED = "Posted", "Posted"
    PAID = "Paid", "Paid"
    CANCELLED = "Cancelled", "Cancelled"
    APPROVED = "Approved", "Approved"  
