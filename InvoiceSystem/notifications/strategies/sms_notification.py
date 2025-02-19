class SMSNotification:
    def notify(self, invoice):
        # Enviar SMS a tesorería
        print(f"Enviando SMS a tesorería para la factura {invoice.id}")
