from io import StringIO
import sys
from django.test import TestCase
from invoice_app.app.invoice_states.cancelled_state import CancelledState
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory

class TestCancelledState(TestCase):

    def test_approve_invoice_from_cancelled(self):
        # Arrange
        cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")
        invoice = InvoiceFactory.create(invoice_number="021", total_value=100.0, state=cancelled_state)
        cancelled = CancelledState()
        
        # Act & Assert
        with self.assertRaises(ValueError):
            cancelled.approve(invoice)

    def test_cancel_invoice_from_cancelled(self):
        # Arrange
        cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")
        invoice = InvoiceFactory.create(invoice_number="022", total_value=0.0, state=cancelled_state)
        cancelled = CancelledState()
        
        # Act & Assert
        with self.assertRaises(ValueError):
            cancelled.cancel(invoice)

    def test_pay_invoice_from_cancelled(self):
        # Arrange
        cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")
        invoice = InvoiceFactory.create(invoice_number="023", total_value=0.0, state=cancelled_state)
        cancelled = CancelledState()
        
        # Act & Assert
        with self.assertRaises(ValueError):
            cancelled.pay(invoice)

    def test_validate_transition_from_cancelled(self):
        # Arrange
        cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")
        invoice = InvoiceFactory.create(invoice_number="024", total_value=0.0, state=cancelled_state)
        cancelled = CancelledState()
        
        # Act & Assert
        with self.assertRaises(ValueError):
            cancelled.validate_transition(invoice, InvoiceStateEnum.APPROVED)

    def test_send_invoice_cancelled_signal(self):
        # Arrange
        cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")
        invoice = InvoiceFactory.create(invoice_number="025", total_value=0.0, state=cancelled_state)
        cancelled = CancelledState()

        # Redirect stdout to capture the print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        # Act: trigger the signal by calling the method that sends it
        cancelled.send_invoice_cancelled_signal(invoice)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Assert
        self.assertIn("Invoice 025 has been cancelled", captured_output.getvalue())
