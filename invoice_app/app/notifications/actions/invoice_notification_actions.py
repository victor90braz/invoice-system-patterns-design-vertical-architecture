
import logging

from django.conf import settings

from invoice_app.app.notifications.accounting_entries_observer import AccountingEntriesObserver
from invoice_app.app.notifications.audit_log_observer import AuditLogObserver
from invoice_app.app.notifications.email_notification_observer import EmailNotificationObserver
from invoice_app.app.notifications.enums.observer_types import ObserverType
from invoice_app.app.notifications.treasury_observer import TreasuryObserver

logger = logging.getLogger(__name__)

class InvoiceNotificationActions:

    def __init__(self):
        self.observers = []
        self._register_observers()

    def _register_observers(self):

        match settings.OBSERVERS:
            case {ObserverType.ACCOUNTING: True}:
                self.add_observer(AccountingEntriesObserver())
            case {ObserverType.TREASURY: True}:
                self.add_observer(TreasuryObserver())
            case {ObserverType.AUDIT_LOG: True}:
                self.add_observer(AuditLogObserver())
            case {ObserverType.EMAIL_NOTIFICATION: True}:
                self.add_observer(EmailNotificationObserver())
            case _:
                raise ValueError("No valid observers found in OBSERVERS.")

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def clear_observers(self):
        self.observers.clear()

    def list_observers(self):
        return [observer.__class__.__name__ for observer in self.observers]

    def process_invoice(self, invoice):
        logger.info(f"Processing invoice {invoice.invoice_number}")
        for observer in self.observers:
            try:
                observer.update(invoice)
            except Exception as e:
                logger.error(f"Observer {observer.__class__.__name__} failed: {e}")
