from InvoiceSystem.invoices.states.base_invoice_state import DraftState, PaidState, PostedState
from InvoiceSystem.invoices.validation.paid_payment_validation import PaidPaymentValidation
from invoices.validation.draft_payment_validation import DraftPaymentValidation
from invoices.validation.posted_payment_validation import PostedPaymentValidation

class Invoice:
    def __init__(self):
        self.state = DraftState()  
    
    def approve(self):
        self.state.approve(self)
    
    def cancel(self):
        self.state.cancel(self)
    
    def pay(self):
        
        match self.state:
            case DraftState():
                validation_strategy = DraftPaymentValidation()
            case PostedState():
                validation_strategy = PostedPaymentValidation()
            case PaidState():
                validation_strategy = PaidPaymentValidation()
            case _:
                raise ValueError("Estado desconocido para pago.")
        
        validation_strategy.validate(self)  
        self.state.pay(self)
 
