from unittest.mock import MagicMock, patch
from django.test import TestCase
from django.db.models.signals import post_save

from InvoiceSystem import settings
from InvoiceSystem.app.modules.invoices.notifications.email_notification_observer import EmailNotificationObserver
from InvoiceSystem.app.modules.invoices.notifications.invoice_processor import InvoiceProcessor
from InvoiceSystem.app.modules.invoices.notifications.accounting_entries_observer import AccountingEntriesObserver
from InvoiceSystem.app.modules.invoices.notifications.audit_log_observer import AuditLogObserver
from InvoiceSystem.app.modules.invoices.notifications.treasury_observer import TreasuryObserver
from InvoiceSystem.app.modules.invoices.notifications.invoice_signals import InvoicePostSaveNotifier
from InvoiceSystem.database.factories.invoice_factory import InvoiceFactory
from InvoiceSystem.models import Invoice

class InvoiceNotificationTest(TestCase):

    def setUp(self):
        """Setup before each test using the factory."""
        self.invoice = InvoiceFactory.create(customer_email="customer@example.com")

        # Create mock observers
        self.accounting_observer = MagicMock(spec=AccountingEntriesObserver)
        self.audit_observer = MagicMock(spec=AuditLogObserver)
        self.treasury_observer = MagicMock(spec=TreasuryObserver)

        # Create invoice processor
        self.processor = InvoiceProcessor()
        self.processor.add_observer(self.accounting_observer)
        self.processor.add_observer(self.audit_observer)
        self.processor.add_observer(self.treasury_observer)

        # Explicitly connect the signal
        post_save.connect(InvoicePostSaveNotifier.notify, sender=Invoice)

    def tearDown(self):
        """Disconnect the signal to prevent cross-test interference."""
        post_save.disconnect(InvoicePostSaveNotifier.notify, sender=Invoice)
        super().tearDown()

    def test_invoice_processor_notifies_observers(self):
        """Test if InvoiceProcessor correctly notifies observers."""
        self.processor.process_invoice(self.invoice)

        # Assert that each observer's update() was called once
        self.accounting_observer.update.assert_called_once_with(self.invoice)
        self.audit_observer.update.assert_called_once_with(self.invoice)
        self.treasury_observer.update.assert_called_once_with(self.invoice)

    @patch("InvoiceSystem.app.modules.invoices.notifications.invoice_processor.InvoiceProcessor.process_invoice")
    def test_post_save_signal_triggers_notifications(self, mock_process):
        """Test if saving an invoice triggers notifications via post_save signal."""
        self.invoice.save()  # Should trigger post_save signal
        mock_process.assert_called_once_with(self.invoice)

    @patch("InvoiceSystem.app.modules.invoices.notifications.email_notification_observer.EmailNotificationObserver.update")
    def test_post_save_triggers_email_notification(self, mock_update):
        """Test if saving an invoice triggers the EmailNotificationObserver."""
        self.invoice.save()  # Should trigger post_save signal
        mock_update.assert_called_once_with(self.invoice)

    @patch("InvoiceSystem.app.modules.invoices.notifications.email_notification_observer.send_mail")
    def test_email_notification_observer_sends_email(self, mock_send_mail):
        """Test if EmailNotificationObserver sends an email with correct details."""
        observer = EmailNotificationObserver()
        observer.update(self.invoice)

        mock_send_mail.assert_called_once_with(
            subject=f"Factura #{self.invoice.id} Generada",
            message=f"Hola, su factura con ID {self.invoice.id} ha sido generada. Gracias por su compra.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.invoice.customer_email]
        )

    @patch("InvoiceSystem.app.modules.invoices.notifications.email_notification_observer.send_mail")
    def test_email_notification_not_sent_if_no_customer_email(self, mock_send_mail):
        """Test if no email is sent when the invoice has no customer email."""
        invoice_without_email = InvoiceFactory.create(customer_email="")
        observer = EmailNotificationObserver()
        observer.update(invoice_without_email)

        mock_send_mail.assert_not_called()