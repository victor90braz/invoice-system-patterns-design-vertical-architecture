from django.dispatch import Signal
from django.dispatch import receiver

invoice_approved = Signal()
invoice_cancelled = Signal()

@receiver(invoice_approved)
def handle_invoice_approved(sender, invoice, **kwargs):
    print(f"Invoice {invoice.invoice_number} has been approved and is now 'posted'.")

@receiver(invoice_cancelled)
def handle_invoice_cancelled(sender, invoice, **kwargs):
    print(f"Invoice {invoice.invoice_number} has been cancelled.")