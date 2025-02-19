class EmailNotification:
    def notify(self, invoice):
        # Enviar notificación por email
        print(f"Enviando email a tesorería para la factura {invoice.id}")

class SMSNotification:
    def notify(self, invoice):
        # Enviar SMS a tesorería
        print(f"Enviando SMS a tesorería para la factura {invoice.id}")
