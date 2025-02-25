from django.test import TestCase
from invoice_app.app.invoice_states.paid_state import PaidState
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory

class TestPaidState(TestCase):

    def test_approve_invoice_from_paid(self):
        # Arrange
        paid_state = InvoiceStateFactory.create(code=InvoiceStateEnum.PAID, description="Paid state")
        invoice = InvoiceFactory.create(invoice_number="009", total_value=0.0, state=paid_state)
        paid = PaidState()

        # Act & Assert
        with self.assertRaises(ValueError):
            paid.approve(invoice)

    def test_cancel_invoice_from_paid(self):
        # Arrange
        paid_state = InvoiceStateFactory.create(code=InvoiceStateEnum.PAID, description="Paid state")
        invoice = InvoiceFactory.create(invoice_number="010", total_value=0.0, state=paid_state)
        paid = PaidState()

        # Act & Assert
        with self.assertRaises(ValueError):
            paid.cancel(invoice)

    def test_pay_invoice_from_paid(self):
        # Arrange
        paid_state = InvoiceStateFactory.create(code=InvoiceStateEnum.PAID, description="Paid state")
        invoice = InvoiceFactory.create(invoice_number="011", total_value=0.0, state=paid_state)
        paid = PaidState()

        # Act & Assert
        with self.assertRaises(ValueError):
            paid.pay(invoice)

    def test_validate_transition_from_paid(self):
        # Arrange
        paid_state = InvoiceStateFactory.create(code=InvoiceStateEnum.PAID, description="Paid state")
        invoice = InvoiceFactory.create(invoice_number="012", total_value=0.0, state=paid_state)
        paid = PaidState()

        # Act & Assert
        # No exception expected since there’s no validation logic for transitions in the Paid state
        try:
            paid.validate_transition(invoice, InvoiceStateEnum.PAID)
        except ValueError:
            self.fail("validate_transition raised ValueError unexpectedly!")
