import factory
from invoice_app.models import InvoiceState

class InvoiceStateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InvoiceState

    name = factory.Faker('word')
    code = factory.Faker('word')
    description = factory.Faker('sentence')
    is_final = factory.Faker('boolean')
    
    @classmethod
    def create_state(cls, name, code, description, is_final=False, **kwargs):
        return cls.create(name=name, code=code, description=description, is_final=is_final, **kwargs)
