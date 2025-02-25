from django.test import TestCase
from invoice_app.app.invoice_states.draft_state import DraftState
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory

class TestDraftStateApprove(TestCase):

    def test_approve_invoice_from_draft(self):
        draft_state = InvoiceStateFactory.create_state(name="Draft", code="draft", description="Draft state")
        posted_state = InvoiceStateFactory.create_state(name="Posted", code="posted", description="Posted state")

        invoice = InvoiceFactory.create(invoice_number="001", total_value=100.0, state=draft_state)

        draft = DraftState()  
        draft.approve(invoice)  

        invoice.refresh_from_db()

        self.assertEqual(invoice.state.code, 'posted')

    def test_cancel_invoice_from_draft(self):
        draft_state = InvoiceStateFactory.create_state(name="Draft", code="draft", description="Draft state")
        cancelled_state = InvoiceStateFactory.create_state(name="Cancelled", code="cancelled", description="Cancelled state")

        invoice = InvoiceFactory.create(invoice_number="002", total_value=0.0, state=draft_state)

        draft = DraftState()  
        draft.cancel(invoice)

        invoice.refresh_from_db()

        self.assertEqual(invoice.state.code, 'cancelled')

    def test_validate_transition_from_draft_to_approved(self):
        draft_state = InvoiceStateFactory.create_state(name="Draft", code="draft", description="Draft state")
        posted_state = InvoiceStateFactory.create_state(name="Posted", code="posted", description="Posted state")

        invoice = InvoiceFactory.create(invoice_number="003", total_value=100.0, state=draft_state)

        draft = DraftState()  
        draft.approve(invoice)

        invoice.refresh_from_db()

        self.assertEqual(invoice.state.code, 'posted')

    def test_validate_transition_from_draft_to_cancelled(self):
        draft_state = InvoiceStateFactory.create_state(name="Draft", code="draft", description="Draft state")
        cancelled_state = InvoiceStateFactory.create_state(name="Cancelled", code="cancelled", description="Cancelled state")

        invoice = InvoiceFactory.create(invoice_number="004", total_value=0.0, state=draft_state)

        draft = DraftState()  
        draft.cancel(invoice)

        invoice.refresh_from_db()

        self.assertEqual(invoice.state.code, 'cancelled')