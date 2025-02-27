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
from invoice_app.database.factories.supplier_factory import SupplierFactory
from invoice_app.models.invoice import Invoice
from invoice_system import settings


class InvoiceNotificationTest(TestCase):

    @patch.object(InvoiceNotificationActions, "resolve_observers")
    def setUp(self, mock_resolve_observers):
        self.invoice = InvoiceFactory.create()

        self.accounting_observer = MagicMock(spec=AccountingEntriesObserver)
        self.audit_observer = MagicMock(spec=AuditLogObserver)
        self.treasury_observer = MagicMock(spec=TreasuryObserver)
        self.email_notification_observer = MagicMock(spec=EmailNotificationObserver)

        mock_resolve_observers.return_value = [
            self.accounting_observer,
            self.audit_observer,
            self.treasury_observer,
            self.email_notification_observer,
        ]

        self.invoice_notification_actions = InvoiceNotificationActions()

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

    @patch.object(InvoiceNotificationActions, "process_invoice")
    def test_post_save_signal_triggers_invoice_notification_actions(self, mock_process):
        # Act
        self.invoice.save()

        # Assert
        mock_process.assert_called_once_with(self.invoice)

    @patch("invoice_app.app.notifications.email_notification_observer.send_mail")
    def test_email_notification_observer_sends_email(self, mock_send_mail):
        # Arrange
        supplier = SupplierFactory.create(email="supplier@example.com")
        invoice = InvoiceFactory.build(supplier=supplier)
        observer = EmailNotificationObserver()

        # Act
        observer.update(invoice)

        # Assert
        mock_send_mail.assert_called_once_with(
            subject=f"Invoice #{invoice.invoice_number} Generated",
            message=f"Hello, your invoice number {invoice.invoice_number} has been generated.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[invoice.supplier.email],
        )

    @patch("invoice_app.app.notifications.email_notification_observer.send_mail")
    def test_email_notification_observer_does_not_send_email_without_email(self, mock_send_mail):
        # Arrange
        supplier = SupplierFactory.create(email=None)
        invoice = InvoiceFactory.create(supplier=supplier)
        observer = EmailNotificationObserver()

        # Act
        observer.update(invoice)

        # Assert
        mock_send_mail.assert_not_called()

    @patch("invoice_app.app.notifications.email_notification_observer.logging.info")
    def test_email_notification_observer_logs_info_when_email_sent(self, mock_logging_info):
        # Arrange
        supplier = SupplierFactory.create(email="supplier@example.com")
        invoice = InvoiceFactory.create(supplier=supplier)
        observer = EmailNotificationObserver()

        # Act
        observer.update(invoice)

        # Assert
        mock_logging_info.assert_any_call(
            f"Email sent to {invoice.supplier.email} for invoice {invoice.invoice_number}."
        )
        self.assertGreaterEqual(mock_logging_info.call_count, 1)

    @patch("invoice_app.app.notifications.email_notification_observer.logging.error")
    def test_email_notification_observer_logs_error_when_email_fails(self, mock_logging_error):
        # Arrange
        supplier = SupplierFactory.create(email="supplier@example.com")
        invoice = InvoiceFactory.create(supplier=supplier)
        observer = EmailNotificationObserver()

        with patch("invoice_app.app.notifications.email_notification_observer.send_mail", side_effect=Exception("Some error")):
            # Act
            observer.update(invoice)

        # Assert
        mock_logging_error.assert_called_once_with(
            f"Failed to send email for invoice {invoice.invoice_number}: Some error"
        )
