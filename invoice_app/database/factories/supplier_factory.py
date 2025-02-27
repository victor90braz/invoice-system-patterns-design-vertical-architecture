import factory
from invoice_app.models.supplier import Supplier
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory

class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    email = factory.Faker("email")
    country = factory.Faker("country_code")

    @factory.post_generation
    def tax_policies(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tax_policies.set(extracted)
        else:
            tax_policies = TaxPolicyFactory.create_batch(2, country=self.country)
            self.tax_policies.set(tax_policies)
