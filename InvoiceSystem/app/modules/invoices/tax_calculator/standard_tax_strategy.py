from InvoiceSystem.app.modules.invoices.interfaces.invoice_tax_calculator_interface import BaseInvoiceTaxCalculatorInterface


class StandardTaxStrategy(BaseInvoiceTaxCalculatorInterface):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.21  # IVA estándar
