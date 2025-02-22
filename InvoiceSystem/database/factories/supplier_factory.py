import factory
from InvoiceSystem.app.modules.invoices.models.supplier import Supplier
from InvoiceSystem.database.factories.tax_policy_factory import TaxPolicyFactory

class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    email = factory.Faker("email")
    tax_policy = factory.SubFactory(TaxPolicyFactory)  