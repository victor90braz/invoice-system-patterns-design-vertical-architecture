import factory
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory
from invoice_app.models.supplier import Supplier

class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    email = factory.Faker("email")

    @factory.post_generation
    def tax_policies(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            self.tax_policies.set(extracted)  # ✅ Usa las `TaxPolicy` pasadas en `extracted`
        else:
            self.tax_policies.add(TaxPolicyFactory.create())  # ✅ Crea una nueva si no se pasó ninguna
