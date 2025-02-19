from .payment_validation_strategy import PaymentValidationStrategy
from invoices.states.posted_state import PostedState

class PostedPaymentValidation(PaymentValidationStrategy):
    def validate(self, invoice):
        if isinstance(invoice.state, PostedState):
            return True
        raise ValueError("Solo se puede pagar una factura en estado contabilizada.")
