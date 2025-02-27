from django.test import TestCase
from invoice_app.app.invoice_states.draft_state import DraftState
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory


class TestDraftStateApprove(TestCase):

    def setUp(self):
        self.draft_state = InvoiceStateFactory.create(code=InvoiceStateEnum.DRAFT, description="Draft state")
        self.posted_state = InvoiceStateFactory.create(code=InvoiceStateEnum.POSTED, description="Posted state")
        self.cancelled_state = InvoiceStateFactory.create(code=InvoiceStateEnum.CANCELLED, description="Cancelled state")

    def test_approve_invoice_from_draft(self):
        # Arrange
        invoice = InvoiceFactory.create(invoice_number="001", total_value=100.0, state=self.draft_state)
        draft = DraftState()

        # Act
        draft.approve(invoice)

        # Assert
        invoice.refresh_from_db()
        self.assertEqual(invoice.state.code, InvoiceStateEnum.POSTED)

    def test_cancel_invoice_from_draft(self):
        # Arrange
        invoice = InvoiceFactory.create(invoice_number="002", total_value=0.0, state=self.draft_state)
        draft = DraftState()

        # Act
        draft.cancel(invoice)

        # Assert
        invoice.refresh_from_db()
        self.assertEqual(invoice.state.code, InvoiceStateEnum.CANCELLED)

    def test_validate_transition_from_draft_to_approved(self):
        # Arrange
        invoice = InvoiceFactory.create(invoice_number="003", total_value=100.0, state=self.draft_state)
        draft = DraftState()

        # Act
        draft.approve(invoice)

        # Assert
        invoice.refresh_from_db()
        self.assertEqual(invoice.state.code, InvoiceStateEnum.POSTED)

    def test_validate_transition_from_draft_to_cancelled(self):
        # Arrange
        invoice = InvoiceFactory.create(invoice_number="004", total_value=0.0, state=self.draft_state)
        draft = DraftState()

        # Act
        draft.cancel(invoice)

        # Assert
        invoice.refresh_from_db()
        self.assertEqual(invoice.state.code, InvoiceStateEnum.CANCELLED)
