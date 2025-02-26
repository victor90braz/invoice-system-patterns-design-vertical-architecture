from unittest.mock import MagicMock, patch
from django.test import TestCase
from django.db.models.signals import post_save

from invoice_app.app.notifications.accounting_entries_observer import AccountingEntriesObserver
from invoice_app.app.notifications.actions.invoice_notification_actions import InvoiceNotificationActions
from invoice_app.app.notifications.audit_log_observer import AuditLogObserver
from invoice_app.app.notifications.email_notification_observer import EmailNotificationObserver
from invoice_app.app.signals.signals import invoicePostSaveNotifier
from invoice_app.app.notifications.treasury_observer import TreasuryObserver
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.models.invoice import Invoice

class InvoiceNotificationTest(TestCase):

    def setUp(self):
        # Arrange
        self.invoice = InvoiceFactory.create()
        self.accounting_observer = MagicMock(spec=AccountingEntriesObserver)
        self.audit_observer = MagicMock(spec=AuditLogObserver)
        self.treasury_observer = MagicMock(spec=TreasuryObserver)
        self.email_notification_observer = MagicMock(spec=EmailNotificationObserver)

        self.invoice_notification_actions = InvoiceNotificationActions()
        self.invoice_notification_actions.add_observer(self.accounting_observer)
        self.invoice_notification_actions.add_observer(self.audit_observer)
        self.invoice_notification_actions.add_observer(self.treasury_observer)
        self.invoice_notification_actions.add_observer(self.email_notification_observer)

        post_save.connect(invoicePostSaveNotifier, sender=Invoice)

    def tearDown(self):
        post_save.disconnect(invoicePostSaveNotifier, sender=Invoice)

    def test_invoice_notification_actions_notifies_observers(self):
        # Act
        self.invoice_notification_actions.process_invoice(self.invoice)

        # Assert
        self.accounting_observer.update.assert_called_once_with(self.invoice)
        self.audit_observer.update.assert_called_once_with(self.invoice)
        self.treasury_observer.update.assert_called_once_with(self.invoice)
        self.email_notification_observer.update.assert_called_once_with(self.invoice)

    @patch.object(InvoiceNotificationActions, 'process_invoice')
    def test_post_save_signal_triggers_invoice_notification_actions(self, mock_process):
        # Act
        self.invoice.save()

        # Assert
        mock_process.assert_called_once_with(self.invoice)
