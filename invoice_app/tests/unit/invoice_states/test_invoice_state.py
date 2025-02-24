from django.test import TestCase
from invoice_app.database.factories.invoice_factory import InvoiceFactory

class TestInvoiceStateTransitions(TestCase):

    def test_invoice_draft_state_approve(self):
        invoice = InvoiceFactory.create(state='draft')
        
        # The invoice should be in draft state initially
        self.assertEqual(invoice.state, 'draft')
        
        # Try to approve the invoice (should transition to "posted")
        invoice.approve()
        invoice.refresh_from_db()  # Reload the instance from the DB
        
        self.assertEqual(invoice.state, 'posted')
    
    def test_invoice_draft_state_cancel(self):
        invoice = InvoiceFactory.create(state='draft')
        
        # The invoice should be in draft state initially
        self.assertEqual(invoice.state, 'draft')
        
        # Try to cancel the invoice (should transition to "cancelled")
        invoice.cancel()
        invoice.refresh_from_db()  # Reload the instance from the DB
        
        self.assertEqual(invoice.state, 'cancelled')
    
    def test_invoice_posted_state_pay(self):
        invoice = InvoiceFactory.create(state='posted')
        
        # The invoice should be in posted state initially
        self.assertEqual(invoice.state, 'posted')
        
        # Try to pay the invoice (should transition to "paid")
        invoice.pay()
        invoice.refresh_from_db()  # Reload the instance from the DB
        
        self.assertEqual(invoice.state, 'paid')
    
    def test_invoice_cancelled_state_approve(self):
        invoice = InvoiceFactory.create(state='cancelled')
        
        # The invoice should be in cancelled state initially
        self.assertEqual(invoice.state, 'cancelled')
        
        # Trying to approve a cancelled invoice should raise an error
        with self.assertRaises(ValueError):
            invoice.approve()
    
    def test_invoice_paid_state_cancel(self):
        invoice = InvoiceFactory.create(state='paid')
        
        # The invoice should be in paid state initially
        self.assertEqual(invoice.state, 'paid')
        
        # Trying to cancel a paid invoice should raise an error
        with self.assertRaises(ValueError):
            invoice.cancel()
    
    def test_invoice_paid_state_approve(self):
        invoice = InvoiceFactory.create(state='paid')
        
        # The invoice should be in paid state initially
        self.assertEqual(invoice.state, 'paid')
        
        # Trying to approve a paid invoice should raise an error
        with self.assertRaises(ValueError):
            invoice.approve()
    
    def test_invoice_posted_state_cancel(self):
        invoice = InvoiceFactory.create(state='posted')
        
        # The invoice should be in posted state initially
        self.assertEqual(invoice.state, 'posted')
        
        # Trying to cancel a posted invoice should raise an error
        with self.assertRaises(ValueError):
            invoice.cancel()
    
    def test_invoice_posted_state_approve(self):
        invoice = InvoiceFactory.create(state='posted')
        
        # The invoice should be in posted state initially
        self.assertEqual(invoice.state, 'posted')
        
        # Trying to approve an already posted invoice should raise an error
        with self.assertRaises(ValueError):
            invoice.approve()
