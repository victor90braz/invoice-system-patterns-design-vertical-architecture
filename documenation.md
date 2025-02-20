# Prueba Técnica: Patrones de Diseño

Este documento describe los patrones de diseño aplicados a diferentes escenarios en un sistema de facturación. Se utilizan los patrones **Estrategia**, **Estado** y **Observador** para resolver problemas específicos relacionados con la generación de asientos, estados de factura, notificaciones y cálculo de impuestos.

---

## Escenario 1: Generación de Asientos

### 1. ¿Qué patrón aplicarías?
- **Patrón Estrategia (Strategy Pattern)**

### 2. ¿Por qué ese patrón?
El patrón Estrategia permite encapsular diferentes algoritmos (reglas de contabilización) en clases separadas. Esto facilita la adición de nuevos tipos de facturas en el futuro sin modificar el código existente, siguiendo el principio de abierto/cerrado (Open/Closed Principle).

### 3. Implementación



### 4. Ventajas
- **Extensibilidad:** Fácil adición de nuevos tipos de facturas.
- **Mantenibilidad:** Cada estrategia está encapsulada.
- **Reutilización:** Las estrategias pueden ser reutilizadas en diferentes partes del sistema.

---

## Escenario 2: Estados de Factura

### 1. ¿Qué patrón aplicarías?
- **Patrón Estado (State Pattern)**

### 2. ¿Por qué ese patrón?
El patrón Estado es adecuado para manejar el comportamiento de un objeto (factura) que cambia según su estado. Cada estado puede tener diferentes reglas de validación y transiciones.

### 3. Implementación

```python
from abc import ABC, abstractmethod

class InvoiceState(ABC):
    @abstractmethod
    def approve(self, invoice):
        pass

    @abstractmethod
    def cancel(self, invoice):
        pass

    @abstractmethod
    def pay(self, invoice):
        pass

class DraftState(InvoiceState):
    def approve(self, invoice):
        print("Factura aprobada desde estado borrador.")
        invoice.state = PostedState()

    def cancel(self, invoice):
        print("Factura cancelada desde estado borrador.")
        invoice.state = CancelledState()

    def pay(self, invoice):
        raise ValueError("No se puede pagar una factura en estado borrador.")

class PostedState(InvoiceState):
    def approve(self, invoice):
        raise ValueError("La factura ya está aprobada.")
    
    def cancel(self, invoice):
        print("Factura cancelada desde estado contabilizado.")
        invoice.state = CancelledState()

    def pay(self, invoice):
        print("Factura pagada desde estado contabilizado.")
        invoice.state = PaidState()

class PaidState(InvoiceState):
    def approve(self, invoice):
        raise ValueError("La factura ya está pagada.")
    
    def cancel(self, invoice):
        raise ValueError("No se puede cancelar una factura ya pagada.")
    
    def pay(self, invoice):
        raise ValueError("La factura ya está pagada.")

class CancelledState(InvoiceState):
    def approve(self, invoice):
        raise ValueError("No se puede aprobar una factura cancelada.")
    
    def cancel(self, invoice):
        raise ValueError("La factura ya está cancelada.")
    
    def pay(self, invoice):
        raise ValueError("No se puede pagar una factura cancelada.")
```

### 4. Ventajas
- **Claridad:** El código relacionado con cada estado está encapsulado.
- **Flexibilidad:** Las transiciones entre estados son manejadas de manera clara.
- **Extensibilidad:** Es fácil añadir nuevos estados o modificar transiciones existentes.

---

## Escenario 3: Notificaciones

### 1. ¿Qué patrón aplicarías?
- **Patrón Observador (Observer Pattern)**

### 2. ¿Por qué ese patrón?
El patrón Observador permite que múltiples objetos (servicios de notificación) sean notificados y actualizados cuando ocurre un evento específico (como la contabilización de una factura). Esto desacopla la lógica de notificación de la lógica de contabilización.

### 3. Implementación

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, invoice):
        pass

class AccountingObserver(Observer):
    def update(self, invoice):
        print(f"Actualizando saldos contables para la factura {invoice.id}")

class TreasuryObserver(Observer):
    def update(self, invoice):
        print(f"Notificando a tesorería sobre la factura {invoice.id}")

class AuditLogObserver(Observer):
    def update(self, invoice):
        print(f"Generando log de auditoría para la factura {invoice.id}")

class Invoice:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def contabilizar(self):
        print("Contabilizando factura...")
        self.notify_observers()
```

### 4. Ventajas
- **Desacoplamiento:** La lógica de notificación está separada de la lógica de contabilización.
- **Extensibilidad:** Es fácil añadir nuevos observadores.
- **Reutilización:** Los observadores pueden ser reutilizados en diferentes partes del sistema.

---

## Escenario 4: Cálculo de Impuestos

### 1. ¿Qué patrón aplicarías?
- **Patrón Estrategia (Strategy Pattern)**

### 2. ¿Por qué ese patrón?
El patrón Estrategia permite encapsular diferentes algoritmos de cálculo de impuestos en clases separadas. Esto facilita la combinación de reglas y la adición de nuevas reglas en el futuro.

### 3. Implementación

```python
from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, invoice):
        pass

class StandardTaxStrategy(TaxStrategy):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.21  # IVA estándar 21%

class ReducedTaxStrategy(TaxStrategy):
    def calculate_tax(self, invoice):
        return invoice.total_value * 0.10  # IVA reducido 10%

class InternationalTaxStrategy(TaxStrategy):
    def calculate_tax(self, invoice):
        return 0  # IVA 0% para ventas internacionales

class CombinedTaxStrategy(TaxStrategy):
    def __init__(self, strategies):
        self.strategies = strategies

    def calculate_tax(self, invoice):
        total_tax = 0
        for strategy in self.strategies:
            total_tax += strategy.calculate_tax(invoice)
        return total_tax
```

### 4. Ventajas
- **Flexibilidad:** Permite combinar diferentes reglas de impuestos.
- **Extensibilidad:** Es fácil añadir nuevas reglas de impuestos.
- **Mantenibilidad:** Cada estrategia está encapsulada.

---

## Conclusión

Los patrones de diseño **Estrategia**, **Estado** y **Observador** proporcionan soluciones robustas y mantenibles para los problemas planteados en los diferentes escenarios. Estos patrones permiten desacoplar la lógica de negocio, facilitar la extensibilidad y mejorar la claridad del código.