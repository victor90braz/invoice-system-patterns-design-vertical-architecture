from django.test import TestCase

from invoice_app.app.accounting_entries.strategies.accounting_entries_driver import AccountingEntriesDriver
from invoice_app.app.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from invoice_app.app.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from invoice_app.app.accounting_entries.strategies.types.invoice_type import InvoiceType
from invoice_app.app.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.supplier_factory import SupplierFactory
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory


class TestAccountingStrategies(TestCase):

    def test_purchase_invoice_generates_purchase_entry(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policies=[tax_policy])
        invoice = InvoiceFactory.create(
            invoice_number="003",
            total_value=500.0,
            invoice_type=InvoiceType.PURCHASE_INVOICE,
            supplier=supplier
        )

        # Act
        strategy = AccountingEntriesDriver.get_strategy(invoice)
        entry = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, PurchaseStrategy)
        self.assertEqual(entry["account"], f"500 - {invoice.invoice_type}")
        self.assertEqual(entry["amount"], invoice.total_value)
        self.assertEqual(entry["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")

    def test_expense_invoice_generates_expense_entry(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policies=[tax_policy])
        invoice = InvoiceFactory.create(
            invoice_number="002",
            total_value=300.0,
            invoice_type=InvoiceType.EXPENSE_INVOICE,
            supplier=supplier
        )

        # Act
        strategy = AccountingEntriesDriver.get_strategy(invoice)
        entry = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, ExpenseStrategy)
        self.assertEqual(entry["account"], f"6000 - {invoice.invoice_type}")
        self.assertEqual(entry["amount"], invoice.total_value)
        self.assertEqual(entry["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")

    def test_investment_invoice_generates_investment_entry(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policies=[tax_policy])
        invoice = InvoiceFactory.create(
            invoice_number="004",
            total_value=1500.0,
            invoice_type=InvoiceType.INVESTMENT_INVOICE,
            supplier=supplier
        )

        # Act
        strategy = AccountingEntriesDriver.get_strategy(invoice)
        entry = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, InvestmentStrategy)
        self.assertEqual(entry["account"], f"100 - {invoice.invoice_type}")
        self.assertEqual(entry["amount"], invoice.total_value)
        self.assertEqual(entry["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")

    def test_unsupported_invoice_type_raises_error(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policies=[tax_policy])
        invoice = InvoiceFactory.create(
            invoice_number="005",
            total_value=200.0,
            invoice_type="UNSUPPORTED_TYPE",
            supplier=supplier
        )

        # Act & Assert
        with self.assertRaises(ValueError):
            AccountingEntriesDriver.get_strategy(invoice)
