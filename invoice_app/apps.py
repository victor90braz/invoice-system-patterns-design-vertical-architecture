from django.apps import AppConfig

class InvoicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invoice_app'  
    label = 'invoice_app'

    def ready(self):
        import invoice_app.app.signals.signals