from django.core.mail import send_mail
from django.conf import settings
import logging

class EmailNotificationObserver:
    def update(self, invoice):

        if invoice.supplier.email:
            try:
                send_mail(
                    subject=f"Invoice #{invoice.id} Generated",
                    message=f"Hello, your invoice with ID {invoice.id} has been generated.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[invoice.supplier.email],
                )
                logging.info(f"Email sent to {invoice.supplier.email} for invoice {invoice.id}.")
            except Exception as e:
                logging.error(f"Failed to send email for invoice {invoice.id}: {e}")
