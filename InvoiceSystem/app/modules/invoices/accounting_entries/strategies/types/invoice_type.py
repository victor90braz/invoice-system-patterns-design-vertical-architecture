from django.db import models

class InvoiceType(models.TextChoices):
    PURCHASE_INVOICE = "purchase_invoice", "Purchase Invoice"
    EXPENSE_INVOICE = "expense_invoice", "Expense Invoice"
    INVESTMENT_INVOICE = "investment_invoice", "Investment Invoice"