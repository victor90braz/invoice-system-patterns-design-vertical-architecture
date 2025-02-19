from abc import ABC, abstractmethod

class BaseInvoiceState(ABC):
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


class DraftState(BaseInvoiceState):
    def approve(self, invoice):
        print("Factura aprobada desde estado borrador.")
        invoice.state = PostedState()

    def cancel(self, invoice):
        print("Factura cancelada desde estado borrador.")
        invoice.state = CancelledState()

    def pay(self, invoice):
        raise ValueError("No se puede pagar una factura en estado borrador.")


class PostedState(BaseInvoiceState):
    def approve(self, invoice):
        raise ValueError("La factura ya está aprobada.")
    
    def cancel(self, invoice):
        print("Factura cancelada desde estado contabilizado.")
        invoice.state = CancelledState()

    def pay(self, invoice):
        print("Factura pagada desde estado contabilizado.")
        invoice.state = PaidState()


class PaidState(BaseInvoiceState):
    def approve(self, invoice):
        raise ValueError("La factura ya está pagada.")
    
    def cancel(self, invoice):
        raise ValueError("No se puede cancelar una factura ya pagada.")
    
    def pay(self, invoice):
        raise ValueError("La factura ya está pagada.")


class CancelledState(BaseInvoiceState):
    def approve(self, invoice):
        raise ValueError("No se puede aprobar una factura cancelada.")
    
    def cancel(self, invoice):
        raise ValueError("La factura ya está cancelada.")
    
    def pay(self, invoice):
        raise ValueError("No se puede pagar una factura cancelada.")
