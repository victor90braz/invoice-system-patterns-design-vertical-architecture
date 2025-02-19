from .base import AccountingEntryStrategy

# Estrategia para Compras (Mercadona)
class MercadonaPurchaseStrategy(AccountingEntryStrategy):
    def generate_entry(self, invoice):
        return {
            "account": "6000 - Compras Mercadona",  # Cuenta para compras
            "amount": invoice.total_value,  # Monto de la factura
            "description": f"Compra Mercadona - Factura {invoice.invoice_number}"  # Descripción
        }
