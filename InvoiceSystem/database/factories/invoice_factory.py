import factory
from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType
from InvoiceSystem.models import Invoice

class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice
    
    invoice_number = factory.Faker('random_number')
    total_value = factory.Faker('random_number', max_digits=5)
    invoice_type = InvoiceType.EXPENSE.value  
    customer_name = factory.Faker('company')
    customer_id = factory.Faker('random_int')

    @classmethod
    def add_invoice_type(cls, invoice_type: InvoiceType, **kwargs):
        return cls.create(invoice_type=invoice_type.value, **kwargs)
