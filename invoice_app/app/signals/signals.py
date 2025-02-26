from django.db.models.signals import post_save
from django.dispatch import Signal, receiver
from invoice_app.models.invoice import Invoice
from invoice_app.app.notifications.accounting_entries_observer import AccountingEntriesObserver
from invoice_app.app.notifications.actions.invoice_notification_actions import InvoiceNotificationActions
from invoice_app.app.notifications.audit_log_observer import AuditLogObserver
from invoice_app.app.notifications.email_notification_observer import EmailNotificationObserver
from invoice_app.app.notifications.treasury_observer import TreasuryObserver

invoice_approved = Signal()
invoice_cancelled = Signal()

@receiver(invoice_approved)
def handle_invoice_approved(sender, invoice, **kwargs):
    print(f"Invoice {invoice.invoice_number} has been approved and is now 'posted'.")

@receiver(invoice_cancelled)
def handle_invoice_cancelled(sender, invoice, **kwargs):
    print(f"Invoice {invoice.invoice_number} has been cancelled.")

@receiver(post_save, sender=Invoice)
def invoicePostSaveNotifier(sender, instance, **kwargs):
    observer = EmailNotificationObserver()
    observer.update(instance)

    processor = InvoiceNotificationActions()
    processor.add_observer(AccountingEntriesObserver())
    processor.add_observer(TreasuryObserver())
    processor.add_observer(AuditLogObserver())
    processor.process_invoice(instance)

