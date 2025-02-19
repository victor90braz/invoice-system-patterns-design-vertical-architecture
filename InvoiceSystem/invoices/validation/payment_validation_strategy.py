from abc import ABC, abstractmethod

class PaymentValidationStrategy(ABC):
    @abstractmethod
    def validate(self, invoice):
        pass