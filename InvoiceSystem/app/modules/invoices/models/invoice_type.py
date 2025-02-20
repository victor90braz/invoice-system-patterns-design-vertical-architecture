from django.db import models

class InvoiceType(models.TextChoices):
    PURCHASE = "purchase", "Purchase"
    EXPENSE = "expense", "Expense"
    INVESTMENT = "investment", "Investment"
