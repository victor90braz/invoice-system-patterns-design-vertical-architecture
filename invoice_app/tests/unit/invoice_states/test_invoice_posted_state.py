from django.test import TestCase
from invoice_app.app.invoice_states.posted_state import PostedState
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory
from invoice_app.models.invoice_state import InvoiceState
from invoice_app.models.invoice import Invoice

class TestPostedState(TestCase):

    def test_approve_invoice_from_posted(self):
        # Arrange
        posted_state = InvoiceStateFactory.create(code=InvoiceStateEnum.POSTED, description="Posted state")
        invoice = InvoiceFactory.create(invoice_number="013", total_value=100.0, state=posted_state)
        posted = PostedState()

        # Act & Assert
        with self.assertRaises(ValueError):
            posted.approve(invoice)

    def test_cancel_invoice_from_posted(self):
        # Arrange
        posted_state = InvoiceStateFactory.create(code=InvoiceStateEnum.POSTED, description="Posted state")
        cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")
        invoice = InvoiceFactory.create(invoice_number="014", total_value=0.0, state=posted_state)
        posted = PostedState()

        # Act
        posted.cancel(invoice)

        # Assert
        invoice.refresh_from_db()
        self.assertEqual(invoice.state.code, InvoiceStateEnum.CANCELLED)

    def test_pay_invoice_from_posted(self):
        # Arrange
        posted_state = InvoiceStateFactory.create(code=InvoiceStateEnum.POSTED, description="Posted state")
        paid_state = InvoiceStateFactory.create(code=InvoiceStateEnum.PAID, description="Paid state")
        invoice = InvoiceFactory.create(invoice_number="015", total_value=100.0, state=posted_state)
        posted = PostedState()

        # Act
        posted.pay(invoice)

        # Assert
        invoice.refresh_from_db()
        self.assertEqual(invoice.state.code, InvoiceStateEnum.PAID)

    def test_validate_transition_from_posted(self):
        # Arrange
        posted_state = InvoiceStateFactory.create(code=InvoiceStateEnum.POSTED, description="Posted state")
        invoice = InvoiceFactory.create(invoice_number="016", total_value=100.0, state=posted_state)
        posted = PostedState()

        # Act & Assert
        try:
            posted.validate_transition(invoice, InvoiceStateEnum.PAID)
        except ValueError:
            self.fail("validate_transition raised ValueError unexpectedly!")
