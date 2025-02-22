import factory
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory
from invoice_app.models.supplier import Supplier


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    email = factory.Faker("email")
    tax_policy = factory.SubFactory(TaxPolicyFactory)  
