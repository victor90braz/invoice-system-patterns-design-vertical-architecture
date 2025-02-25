from django.test import TestCase
from invoice_app.app.invoice_states.draft_state import DraftState
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory
from django.core.exceptions import ValidationError

class TestDraftStateApprove(TestCase):

    def test_approve_invoice_from_draft(self):
        
        draft_state = InvoiceStateFactory.create_state(name="Draft", code="draft", description="Factura en borrador")
        InvoiceStateFactory.create_state(name="Posted", code="posted", description="Factura publicada")
        
        invoice = InvoiceFactory.create(invoice_number="001", total_value=100.0, state=draft_state)

        draft = DraftState()  
        draft.approve(invoice)  

        invoice.refresh_from_db()

        self.assertEqual(invoice.state.code, 'posted')



