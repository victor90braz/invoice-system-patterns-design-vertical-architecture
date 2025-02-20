from InvoiceSystem.app.modules.invoices.interfaces.invoice_tax_calculator_interface import BaseInvoiceTaxCalculatorInterface


class InternationalTaxStrategy(BaseInvoiceTaxCalculatorInterface):
    def calculate_tax(self, invoice):
        return 0  # IVA 0% para ventas internacionales
