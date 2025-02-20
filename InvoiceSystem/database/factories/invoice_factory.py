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
    def define_as_expense_invoice(cls, **kwargs):
        """Define the invoice type as 'expense'."""
        return cls.create(invoice_type='expense', **kwargs)

    @classmethod
    def define_as_purchase_invoice(cls, **kwargs):
        """Define the invoice type as 'purchase'."""
        return cls.create(invoice_type='purchase', **kwargs)

    @classmethod
    def define_as_investment_invoice(cls, **kwargs):
        """Define the invoice type as 'investment'."""
        return cls.create(invoice_type='investment', **kwargs)
