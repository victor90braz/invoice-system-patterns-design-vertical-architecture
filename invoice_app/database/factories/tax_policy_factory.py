from decimal import Decimal
import random
import factory
from invoice_app.models.tax_policy import TaxPolicy

class TaxPolicyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaxPolicy

    rate = factory.LazyFunction(lambda: Decimal(random.choice(["21.00", "10.00", "15.00"])))
    product_type = factory.Iterator(["electronics", "food", "clothing", "software", "books"])
    tax_regime = factory.Iterator(["freelancer", "corporate", "government"])
    country = factory.Iterator(["US", "CA", "GB", "DE", "FR"])  
 