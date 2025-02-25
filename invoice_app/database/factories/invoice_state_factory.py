import factory
from invoice_app.models import InvoiceState
from invoice_app.app.invoice_states.enums.invoice_state_enums import InvoiceStateEnum

class InvoiceStateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InvoiceState

    code = factory.Faker('word')
    description = factory.Faker('sentence')

