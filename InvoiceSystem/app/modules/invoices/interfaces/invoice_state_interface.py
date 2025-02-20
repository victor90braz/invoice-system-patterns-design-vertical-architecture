from abc import ABC, abstractmethod

class BaseInvoiceStateInterface(ABC):
    """Interfaz base para los estados de una factura."""

    @abstractmethod
    def approve(self, invoice):
        """Transición a estado aprobado."""
        pass

    @abstractmethod
    def cancel(self, invoice):
        """Transición a estado cancelado."""
        pass

    @abstractmethod
    def pay(self, invoice):
        """Transición a estado pagado."""
        pass

    def __str__(self):
        """Devuelve el nombre del estado como string."""
        return self.__class__.__name__











