import factory
from invoice_app.models.tax_policy import TaxPolicy

class TaxPolicyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaxPolicy

    product_type = factory.Faker("word", ext_word_list=["goods", "services", "other"])
    country = factory.Faker("country")
    tax_regime = factory.Faker("word")
    tax_rate = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True, min_value=0.01)
