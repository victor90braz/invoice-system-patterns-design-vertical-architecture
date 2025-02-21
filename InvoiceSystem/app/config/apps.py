from django.apps import AppConfig
from django.db.models.signals import post_save
from InvoiceSystem.models import Invoice
from InvoiceSystem.app.modules.invoices.notifications.invoice_signals import InvoicePostSaveNotifier

class InvoiceSystemConfig(AppConfig):
    name = 'InvoiceSystem'

    def ready(self):
        post_save.connect(InvoicePostSaveNotifier.notify, sender=Invoice)
