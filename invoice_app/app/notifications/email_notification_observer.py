from django.core.mail import send_mail
from django.conf import settings
import logging

from invoice_app.models.invoice import Invoice

class EmailNotificationObserver:
    def update(self, invoice: Invoice):

        if invoice.supplier.email:
            try:
                send_mail(
                    subject=f"Invoice #{invoice.invoice_number} Generated",
                    message=f"Hello, your invoice number {invoice.invoice_number} has been generated.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[invoice.supplier.email],
                )
                logging.info(f"Email sent to {invoice.supplier.email} for invoice {invoice.invoice_number}.")
            except Exception as error:
                logging.error(f"Failed to send email for invoice {invoice.invoice_number}: {error}")
