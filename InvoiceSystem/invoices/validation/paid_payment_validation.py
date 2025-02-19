from .payment_validation_strategy import PaymentValidationStrategy
from invoices.states.paid_state import PaidState

class PaidPaymentValidation(PaymentValidationStrategy):
    def validate(self, invoice):
        if isinstance(invoice.state, PaidState):
            raise ValueError("No se puede pagar una factura que ya está pagada.")
        return True
