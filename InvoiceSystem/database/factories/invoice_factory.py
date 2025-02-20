import factory
from InvoiceSystem.models import Invoice

class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice
    
    invoice_number = factory.Faker('random_number')
    total_value = factory.Faker('random_number', max_digits=5)
    invoice_type = 'expense'  # Default type, can be overridden
    customer_name = factory.Faker('company')
    customer_id = factory.Faker('random_int')

    @classmethod
    def create_expense(cls, **kwargs):
        """Create a 'expense' type invoice."""
        return cls.create(invoice_type='expense', **kwargs)

    @classmethod
    def create_purchase(cls, **kwargs):
        """Create a 'purchase' type invoice."""
        return cls.create(invoice_type='purchase', **kwargs)

    @classmethod
    def create_investment(cls, **kwargs):
        """Create an 'investment' type invoice."""
        return cls.create(invoice_type='investment', **kwargs)
