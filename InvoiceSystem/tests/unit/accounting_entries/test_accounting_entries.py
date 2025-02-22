from django.test import TestCase
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.expense_strategy import ExpenseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.purchase_strategy import PurchaseStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.types.investment_strategy import InvestmentStrategy
from InvoiceSystem.app.modules.invoices.accounting_entries.strategies.accounting_entries_driver import AccountingEntriesDriver
from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType
from InvoiceSystem.database.factories.invoice_factory import InvoiceFactory
from InvoiceSystem.database.factories.supplier_factory import SupplierFactory
from InvoiceSystem.database.factories.tax_policy_factory import TaxPolicyFactory


class TestAccountingStrategies(TestCase):

    def test_purchase_invoice_generates_purchase_entry(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policy=tax_policy)
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
        supplier = SupplierFactory.create(tax_policy=tax_policy)
        invoice = InvoiceFactory.create(
            invoice_number="002",
            total_value=300.0,
            invoice_type=InvoiceType.EXPENSE_INVOICE,
            supplier=supplier
        )

        # Act
        strategy = AccountingEntriesDriver.get_strategy(invoice)
        result = strategy.generate_entry(invoice)

        # Assert
        self.assertIsInstance(strategy, ExpenseStrategy)
        self.assertEqual(result["account"], f"6000 - {invoice.invoice_type}")
        self.assertEqual(result["amount"], invoice.total_value)
        self.assertEqual(result["description"], f"Generated type: {invoice.invoice_type}, Invoice Number - {invoice.invoice_number}")

    def test_investment_invoice_generates_investment_entry(self):
        # Arrange
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policy=tax_policy)
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
        tax_policy = TaxPolicyFactory.create()
        supplier = SupplierFactory.create(tax_policy=tax_policy)
        invoice = InvoiceFactory.create(
            invoice_number="005",
            total_value=200.0,
            invoice_type="UNSUPPORTED_TYPE",
            supplier=supplier
        )
        with self.assertRaises(ValueError):
            AccountingEntriesDriver.get_strategy(invoice)
