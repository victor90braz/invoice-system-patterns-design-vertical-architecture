from InvoiceSystem.accounting.strategies.base import AccountingEntryStrategy

# Estrategia para Inversiones
class InvestmentStrategy(AccountingEntryStrategy):
    def generate_entry(self, invoice):
        return {
            "account": "8000 - Inversiones",  # Cuenta para inversiones
            "amount": invoice.total_value,  # Monto de la factura
            "description": f"Inversión - Factura {invoice.invoice_number}"  # Descripción
        }