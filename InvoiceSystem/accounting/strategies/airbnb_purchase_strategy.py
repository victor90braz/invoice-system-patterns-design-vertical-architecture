from InvoiceSystem.accounting.strategies.base import AccountingEntryStrategy

# Estrategia para Gastos (Airbnb)
class AirbnbExpenseStrategy(AccountingEntryStrategy):
    def generate_entry(self, invoice):
        return {
            "account": "7000 - Gastos Airbnb",  # Cuenta para gastos
            "amount": invoice.total_value,  # Monto de la factura
            "description": f"Gasto Airbnb - Factura {invoice.invoice_number}"  # Descripción
        }