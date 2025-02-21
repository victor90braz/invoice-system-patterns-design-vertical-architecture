import factory
from InvoiceSystem.app.modules.invoices.models.invoice_type import InvoiceType
from InvoiceSystem.models import Invoice


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    invoice_number = factory.Faker("random_number", digits=5, fix_len=True)
    total_value = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    invoice_type = factory.Iterator([InvoiceType.EXPENSE_INVOICE.value, InvoiceType.PURCHASE_INVOICE.value])
    customer_name = factory.Faker("company")
    customer_id = factory.Faker("random_int", min=1, max=9999)
    customer_email = factory.Faker("email")  

    @classmethod
    def add_invoice_type(cls, invoice_type: InvoiceType, **kwargs):
        return cls.create(invoice_type=invoice_type.value, **kwargs)
