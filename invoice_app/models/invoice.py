from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from invoice_app.app.accounting_entries.strategies.types.invoice_type import InvoiceType
from invoice_app.app.invoice_states.draft_state import DraftState
from invoice_app.app.invoice_states.paid_state import PaidState
from invoice_app.app.invoice_states.cancelled_state import CancelledState
from invoice_app.app.invoice_states.posted_state import PostedState  # Add this if you're using it
from invoice_app.models.supplier import Supplier


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    invoice_type = models.CharField(
        max_length=20,
        choices=InvoiceType.choices,
        default=InvoiceType.PURCHASE_INVOICE,
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="invoices")
    state = models.CharField(
            max_length=100,  # Increase the length here
            choices=[('draft', 'Draft'), ('paid', 'Paid'), ('cancelled', 'Cancelled'), ('posted', 'Posted')],
            default='draft'
        )
    
    def clean(self):
        super().clean()
        if Invoice.objects.exclude(id=self.id).filter(invoice_number=self.invoice_number).exists():
            raise ValidationError({'invoice_number': 'Invoice number must be unique.'})

    def __str__(self):
        return f"Invoice {self.invoice_number} (Total: {self.total_value})"

    def approve(self):
        # Before transitioning, validate the transition to the new state
        self.validate_transition('posted')
        current_state = self.get_current_state()
        current_state.approve(self)
        self.state = 'posted'
        self.save()

    def cancel(self):
        # Before transitioning, validate the transition to the cancelled state
        self.validate_transition('cancelled')
        current_state = self.get_current_state()
        current_state.cancel(self)
        self.state = 'cancelled'
        self.save()

    def pay(self):
        # Before transitioning, validate the transition to the paid state
        self.validate_transition('paid')
        current_state = self.get_current_state()
        current_state.pay(self)
        self.state = 'paid'
        self.save()

    def get_current_state(self):
        state_classes = {
            'draft': DraftState(),
            'paid': PaidState(),
            'cancelled': CancelledState(),
            'posted': PostedState(),  # Ensure you have this class or remove it if not
        }
        state_class = state_classes.get(self.state)

        if not state_class:
            raise ValueError(f"Invalid state '{self.state}' for invoice {self.invoice_number}")

        return state_class

    def validate_transition(self, target_state):
        """Validates transition to a new state before applying it."""
        current_state = self.get_current_state()
        current_state.validate_transition(self, target_state)
