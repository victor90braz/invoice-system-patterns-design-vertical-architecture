from InvoiceSystem.models import Invoice
from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class EmailNotificationObserver(BaseAccountingEntriesObserverInterface):

    def update(self, invoice: Invoice):

        if not invoice.supplier.email:
            logger.warning(f"No email sent: Invoice {invoice.id} has no supplier email.")
            return
        
        subject = f"Invoice #{invoice.id} Generated"
        message = f"Hello, your invoice with ID {invoice.id} has been generated. Thank you for your purchase."

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [invoice.supplier.email]  

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list
            )
            logger.info(f"Email sent to {invoice.supplier.email} for invoice {invoice.id}.")
        except Exception as e:
            logger.error(f"Failed to send email for invoice {invoice.id}: {e}")
