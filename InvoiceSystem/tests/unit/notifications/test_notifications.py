from unittest.mock import MagicMock, patch
from django.test import TestCase
from django.db.models.signals import post_save

from InvoiceSystem import settings
from InvoiceSystem.app.modules.invoices.notifications.email_notification_observer import EmailNotificationObserver
from InvoiceSystem.app.modules.invoices.notifications.actions.invoice_notification_actions import InvoiceNotificationActions
from InvoiceSystem.app.modules.invoices.notifications.accounting_entries_observer import AccountingEntriesObserver
from InvoiceSystem.app.modules.invoices.notifications.audit_log_observer import AuditLogObserver
from InvoiceSystem.app.modules.invoices.notifications.treasury_observer import TreasuryObserver
from InvoiceSystem.app.modules.invoices.notifications.invoice_signals import InvoicePostSaveNotifier
from InvoiceSystem.database.factories.invoice_factory import InvoiceFactory
from InvoiceSystem.app.modules.invoices.models.invoice import Invoice


class InvoiceNotificationTest(TestCase):

    def setUp(self):
        # Arrange
        self.invoice = InvoiceFactory.create()
        self.accounting_observer = MagicMock(spec=AccountingEntriesObserver)
        self.audit_observer = MagicMock(spec=AuditLogObserver)
        self.treasury_observer = MagicMock(spec=TreasuryObserver)

        self.notification_manager = InvoiceNotificationActions()
        self.notification_manager.add_observer(self.accounting_observer)
        self.notification_manager.add_observer(self.audit_observer)
        self.notification_manager.add_observer(self.treasury_observer)

        post_save.connect(InvoicePostSaveNotifier.notify, sender=Invoice)

    def tearDown(self):
        post_save.disconnect(InvoicePostSaveNotifier.notify, sender=Invoice)

    def test_invoice_notification_actions_notifies_observers(self):
        # Act
        self.notification_manager.process_invoice(self.invoice)

        # Assert
        self.accounting_observer.update.assert_called_once_with(self.invoice)
        self.audit_observer.update.assert_called_once_with(self.invoice)
        self.treasury_observer.update.assert_called_once_with(self.invoice)

    @patch("InvoiceSystem.app.modules.invoices.notifications.actions.invoice_notification_actions.InvoiceNotificationActions.process_invoice")
    def test_post_save_signal_triggers_invoice_notification_actions(self, mock_process):
        # Act
        self.invoice.save()

        # Assert
        mock_process.assert_called_once_with(self.invoice)

    @patch("InvoiceSystem.app.modules.invoices.notifications.email_notification_observer.EmailNotificationObserver.update")
    def test_post_save_triggers_email_notification(self, mock_update):
        # Act
        self.invoice.save()

        # Assert
        mock_update.assert_called_once_with(self.invoice)

    @patch("InvoiceSystem.app.modules.invoices.notifications.email_notification_observer.send_mail")
    def test_email_notification_observer_sends_email(self, mock_send_mail):
        # Arrange
        observer = EmailNotificationObserver()

        # Act
        observer.update(self.invoice)

        # Assert
        mock_send_mail.assert_called_once_with(
            subject=f"Invoice #{self.invoice.id} Generated",
            message=f"Hello, your invoice with ID {self.invoice.id} has been generated. Thank you for your purchase.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.invoice.supplier.email],
        )

    @patch("InvoiceSystem.app.modules.invoices.notifications.email_notification_observer.send_mail")
    def test_email_notification_not_sent_if_no_supplier_email(self, mock_send_mail):
        # Arrange
        self.invoice.supplier.email = ""
        self.invoice.supplier.save()
        observer = EmailNotificationObserver()

        # Act
        observer.update(self.invoice)

        # Assert
        mock_send_mail.assert_not_called()
