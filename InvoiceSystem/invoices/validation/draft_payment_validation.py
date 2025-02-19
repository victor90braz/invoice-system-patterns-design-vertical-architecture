from .payment_validation_strategy import PaymentValidationStrategy
from invoices.states.draft_state import DraftState

class DraftPaymentValidation(PaymentValidationStrategy):
    def validate(self, invoice):
        if isinstance(invoice.state, DraftState):
            raise ValueError("No se puede pagar una factura en estado borrador.")
        return True
