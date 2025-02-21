from django.db.models.signals import post_save
from InvoiceSystem.app.modules.invoices.notifications.accounting_entries_observer import AccountingEntriesObserver
from InvoiceSystem.app.modules.invoices.notifications.audit_log_observer import AuditLogObserver
from InvoiceSystem.app.modules.invoices.notifications.invoice_processor import InvoiceProcessor
from InvoiceSystem.app.modules.invoices.notifications.treasury_observer import TreasuryObserver
from InvoiceSystem.app.modules.invoices.notifications.email_notification_observer import EmailNotificationObserver

class InvoicePostSaveNotifier:
    
    @staticmethod
    def notify(sender, instance, **kwargs):
        observer = EmailNotificationObserver()
        observer.update(instance)

        processor = InvoiceProcessor()
        processor.add_observer(AccountingEntriesObserver())
        processor.add_observer(AuditLogObserver())
        processor.add_observer(TreasuryObserver())
        processor.process_invoice(instance)