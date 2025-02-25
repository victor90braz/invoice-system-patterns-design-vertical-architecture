import factory
from invoice_app.app.accounting_entries.strategies.types.invoice_type import InvoiceType
from invoice_app.database.factories.supplier_factory import SupplierFactory
from invoice_app.database.factories.invoice_state_factory import InvoiceStateFactory
from invoice_app.models.invoice import Invoice

class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    invoice_number = factory.Faker("random_number", digits=5, fix_len=True)
    total_value = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    invoice_type = factory.Iterator([InvoiceType.EXPENSE_INVOICE.value, InvoiceType.PURCHASE_INVOICE.value])
    supplier = factory.SubFactory(SupplierFactory)
    state = factory.SubFactory(InvoiceStateFactory) 

    @classmethod
    def add_invoice_type(cls, invoice_type: InvoiceType, **kwargs):
        return cls.create(invoice_type=invoice_type.value, **kwargs)
