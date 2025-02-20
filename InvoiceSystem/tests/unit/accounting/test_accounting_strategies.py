from django.test import TestCase
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from InvoiceSystem.database.factories.invoice_factory import InvoiceFactory
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.accounting_strategy_helper import AccountingStrategyHelper

class TestAccountingStrategies(TestCase):

    def test_expense_invoice_accounting_entry(self):

        # Arrange
        invoice = InvoiceFactory.create_expense(
            invoice_number="002", 
            total_value=300.0
        )
        
        # Act
        strategy = AccountingStrategyHelper.get_strategy(invoice)
        result = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, ExpenseStrategy)  
        self.assertEqual(result["account"], f"6000 - {invoice.invoice_type}")  
        self.assertEqual(result["amount"], invoice.total_value)  
        self.assertEqual(result["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")  

    def test_purchase_invoice_accounting_entry(self):

        # Arrange
        invoice = InvoiceFactory.create_purchase(invoice_number="003", total_value=500.0)

        # Act
        strategy = AccountingStrategyHelper.get_strategy(invoice)
        entry = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, PurchaseStrategy)  
        self.assertEqual(entry["account"], f"500 - {invoice.invoice_type}")  
        self.assertEqual(entry["amount"], invoice.total_value)  
        self.assertEqual(entry["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")  

    def test_investment_invoice_accounting_entry(self):

        # Arrange
        invoice = InvoiceFactory.create_investment(invoice_number="004", total_value=1500.0)

        # Act
        strategy = AccountingStrategyHelper.get_strategy(invoice)
        entry = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, InvestmentStrategy)  
        self.assertEqual(entry["account"], f"100 - {invoice.invoice_type}")  
        self.assertEqual(entry["amount"], invoice.total_value)  
        self.assertEqual(entry["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")  

    def test_invalid_invoice_type(self):

        # Arrange
        invoice = InvoiceFactory.create(
            invoice_number="005", 
            total_value=200.0, 
            invoice_type="unsupported",  
            customer_name="Nonexistent Corp.",  
            customer_id=5
        )

        # Act & Assert
        with self.assertRaises(ValueError):
            AccountingStrategyHelper.get_strategy(invoice)
