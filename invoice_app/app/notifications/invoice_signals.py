from invoice_app.app.notifications.accounting_entries_observer import AccountingEntriesObserver
from invoice_app.app.notifications.actions.invoice_notification_actions import InvoiceNotificationActions
from invoice_app.app.notifications.audit_log_observer import AuditLogObserver
from invoice_app.app.notifications.email_notification_observer import EmailNotificationObserver
from invoice_app.app.notifications.treasury_observer import TreasuryObserver


class InvoicePostSaveNotifier:
    
    @staticmethod
    def notify(sender, instance, **kwargs):
        observer = EmailNotificationObserver()
        observer.update(instance)

        processor = InvoiceNotificationActions()
        processor.add_observer(AccountingEntriesObserver())
        processor.add_observer(TreasuryObserver())
        processor.add_observer(AuditLogObserver())
        processor.process_invoice(instance)