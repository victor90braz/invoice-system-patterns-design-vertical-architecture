class TreasuryObserver:
    def update(self, invoice):
        # Lógica para notificar a tesorería
        print(f"Notificando a tesorería sobre la factura {invoice.id}")
