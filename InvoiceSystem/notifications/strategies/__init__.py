class EmailNotification:
    def notify(self, invoice):
        # Enviar notificación por email
        print(f"Enviando email a tesorería para la factura {invoice.id}")
