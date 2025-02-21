from InvoiceSystem.app.modules.invoices.notifications.accounting_entries_observer import AccountingEntriesObserver
from InvoiceSystem.app.modules.invoices.notifications.audit_log_observer import AuditLogObserver
from InvoiceSystem.app.modules.invoices.notifications.actions.invoice_notification_actions import InvoiceNotificationActions
from InvoiceSystem.app.modules.invoices.notifications.treasury_observer import TreasuryObserver
from InvoiceSystem.app.modules.invoices.notifications.email_notification_observer import EmailNotificationObserver

class InvoicePostSaveNotifier:
    
    @staticmethod
    def notify(sender, instance, **kwargs):
        observer = EmailNotificationObserver()
        observer.update(instance)

        processor = InvoiceNotificationActions()
        processor.add_observer(AccountingEntriesObserver())
        processor.add_observer(AuditLogObserver())
        processor.add_observer(TreasuryObserver())
        processor.process_invoice(instance)