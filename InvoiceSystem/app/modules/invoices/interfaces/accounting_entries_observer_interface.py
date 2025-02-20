from abc import ABC, abstractmethod

class BaseAccountingEntriesObserverInterface(ABC):
    @abstractmethod
    def update(self, invoice):
        pass