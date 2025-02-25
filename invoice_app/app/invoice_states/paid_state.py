from django.db.models.signals import post_save
from django.dispatch import receiver
from invoice_app.app.interfaces.invoice_state_interface import BaseInvoiceStateInterface
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum
from invoice_app.models.invoice import Invoice

class PaidState(BaseInvoiceStateInterface):

    def approve(self, invoice: Invoice):
        raise ValueError(f"Invoice {invoice.invoice_number} is already paid. It cannot be approved.")

    def cancel(self, invoice: Invoice):
        raise ValueError(f"Invoice {invoice.invoice_number} cannot be cancelled because it is already paid.")

    def pay(self, invoice: Invoice):
        raise ValueError(f"Invoice {invoice.invoice_number} is already paid.")

    def validate_transition(self, invoice: Invoice, target_state: str):
        pass

    @receiver(post_save, sender=Invoice)
    def handle_invoice_paid_state(sender, instance, created, **kwargs):
        if instance.state.code == InvoiceStateEnum.PAID:

            if not instance._state.adding:  
                return
            
            instance.total_value = 0.0
            instance.save()
