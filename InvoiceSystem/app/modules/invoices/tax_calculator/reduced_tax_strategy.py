from InvoiceSystem.app.modules.invoices.interfaces.invoice_tax_calculator_interface import BaseInvoiceTaxCalculatorInterface


class ReducedTaxStrategy(BaseInvoiceTaxCalculatorInterface):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.10  # IVA reducido
