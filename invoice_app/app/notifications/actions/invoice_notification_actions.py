import logging
from django.conf import settings

from invoice_app.app.notifications.accounting_entries_observer import AccountingEntriesObserver
from invoice_app.app.notifications.audit_log_observer import AuditLogObserver
from invoice_app.app.notifications.email_notification_observer import EmailNotificationObserver
from invoice_app.app.notifications.enums.observer_types import ObserverType
from invoice_app.app.notifications.treasury_observer import TreasuryObserver

logger = logging.getLogger(__name__)

class InvoiceNotificationActions:
    OBSERVER_MAPPING = {
        ObserverType.ACCOUNTING: AccountingEntriesObserver,
        ObserverType.TREASURY: TreasuryObserver,
        ObserverType.AUDIT_LOG: AuditLogObserver,
        ObserverType.EMAIL_NOTIFICATION: EmailNotificationObserver,
    }

    def __init__(self):
        self.observers = self.resolve_observers()

    def resolve_observers(self):
        if not isinstance(settings.OBSERVERS, dict):
            logger.error("OBSERVERS setting must be a dictionary.")
            return []

        return [
            observer_class() for observer_type, observer_class in self.OBSERVER_MAPPING.items()
            if settings.OBSERVERS.get(observer_type, False)
        ]

    def list_observers(self):
        return [observer.__class__.__name__ for observer in self.observers]

    def process_invoice(self, invoice):
        logger.info(f"Processing invoice {invoice.invoice_number} with observers: {self.list_observers()}")
        for observer in self.observers:
            try:
                observer.update(invoice)
            except Exception as error:
                logger.error(f"Observer {observer.__class__.__name__} failed: {error}")
