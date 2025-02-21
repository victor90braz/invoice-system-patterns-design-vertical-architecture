from InvoiceSystem.models import Invoice
from InvoiceSystem.app.modules.invoices.interfaces.accounting_entries_observer_interface import BaseAccountingEntriesObserverInterface
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class EmailNotificationObserver(BaseAccountingEntriesObserverInterface):

    def update(self, invoice: Invoice):

        if not invoice.customer_email:
            logger.warning(f"No email sent: Invoice {invoice.id} has no customer email.")
            return
        
        subject = f"Factura #{invoice.id} Generada"
        message = f"Hola, su factura con ID {invoice.id} ha sido generada. Gracias por su compra."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [invoice.customer_email]

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list
            )
            logger.info(f"Email sent to {invoice.customer_email} for invoice {invoice.id}.")
        except Exception as e:
            logger.error(f"Failed to send email for invoice {invoice.id}: {e}")