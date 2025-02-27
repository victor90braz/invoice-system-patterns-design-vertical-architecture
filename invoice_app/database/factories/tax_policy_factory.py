import factory
from invoice_app.models.tax_policy import TaxPolicy

class TaxPolicyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaxPolicy

    rate = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True, min_value=0.01, max_value=25.00)
    product_type = factory.Iterator(["electronics", "food", "clothing"])
    tax_regime = factory.Faker("word", ext_word_list=["freelancer", "corporate", "government"])
