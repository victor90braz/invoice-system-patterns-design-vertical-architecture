from abc import ABC, abstractmethod

# Estrategia Base para la generación de asientos contables
class AccountingEntryStrategy(ABC):
    @abstractmethod
    def generate_entry(self, invoice):
        pass