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
    product_type = factory.Faker("word", ext_word_list=["goods", "services", "other"])
    supplier_country = factory.Faker("country")
    tax_regime = factory.Faker("word")

    @classmethod
    def add_invoice_type(cls, invoice_type: InvoiceType, **kwargs):
        """Adds invoice type to the factory."""
        return cls.create(invoice_type=invoice_type.value, **kwargs)

    @classmethod
    def add_product_type(cls, product_type: str, **kwargs):
        """Sets the product type for the given invoice."""
        invoice = kwargs.get('invoice')
        if invoice:
            invoice.product_type = product_type
            invoice.save()
        return invoice

    @classmethod
    def add_supplier_country(cls, supplier_country: str, **kwargs):
        """Sets the supplier country for the given invoice."""
        invoice = kwargs.get('invoice')
        if invoice:
            invoice.supplier_country = supplier_country[:50] 
            invoice.save()
        return invoice

    @classmethod
    def add_tax_regime(cls, tax_regime: str, **kwargs):
        """Sets the tax regime for the given invoice."""
        invoice = kwargs.get('invoice')
        if invoice:
            invoice.tax_regime = tax_regime
            invoice.save()
        return invoice
