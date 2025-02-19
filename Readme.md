
```markdown
# InvoiceSystem

InvoiceSystem es un sistema de ejemplo desarrollado con Django que implementa una **arquitectura vertical** y utiliza diversos **patrones de diseño** (Strategy, Factory, State, Observer y Chain of Responsibility) para gestionar:

- **Generación de asientos contables** (diferentes tipos de facturas: compras, gastos, inversiones)
- **Estados de factura** (borrador, contabilizada, pagada, anulada)
- **Notificaciones** (Observer / Pub-Sub)
- **Cálculo de impuestos** (Strategy o Chain of Responsibility)

El sistema está orientado a satisfacer las necesidades de empresas como **Mercadona** y **Airbnb**, permitiendo personalizar las reglas de negocio según cada cliente.

## Características

- **Arquitectura Vertical:** Organización del código por funcionalidades: `invoices`, `accounting`, `notifications`, `taxes` y `common`.
- **Patrones de Diseño:**
  - **Strategy + Factory:** Para la generación de asientos contables.
  - **State:** Para la gestión del ciclo de vida de las facturas.
  - **Observer:** Para la gestión de notificaciones ante eventos importantes.
  - **Strategy / Chain of Responsibility:** Para el cálculo de impuestos.
- **Modularidad y Escalabilidad:** Fácil incorporación de nuevas funcionalidades o adaptaciones a diferentes empresas sin modificar la base del sistema.

## Requisitos

- Python 3.x
- Django 3.x o superior
- pip

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <https://github.com/victor90braz/invoice-system-patterns-design-vertical-architecture.git>
   cd InvoiceSystem
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar las migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional, para acceder al panel de administración):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Levantar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

```plaintext
InvoiceSystem/
│
├── invoices/                      # Escenario 2: Estados de Factura (State)
│   ├── controllers/               # Controladores para la gestión de facturas
│   │   └── invoice_controller.py
│   ├── models/                    # Modelo de Factura
│   │   └── invoice.py
│   ├── states/                    # Implementación del patrón State
│   │   ├── base_invoice_state.py
│   │   ├── draft_state.py
│   │   ├── posted_state.py
│   │   ├── paid_state.py
│   │   └── canceled_state.py
│   ├── services/                  # Lógica de negocio de facturas
│   │   └── invoice_service.py
│   ├── dtos/                      # DTOs para la facturación
│   │   └── invoice_dto.py
│   ├── enums/                     # Enumeraciones de estados de factura
│   │   └── invoice_status_enum.py
│   └── utils/                     # Utilidades y validaciones
│       └── invoice_validations.py
│
├── accounting/                    # Escenario 1: Generación de Asientos (Strategy + Factory)
│   ├── controllers/               # Controladores de contabilidad
│   │   └── accounting_controller.py
│   ├── services/                  # Lógica de negocio para asientos contables
│   │   └── accounting_service.py
│   ├── strategies/                # Estrategias para contabilización
│   │   ├── base.py
│   │   ├── mercadona_purchase_strategy.py
│   │   ├── mercadona_expense_strategy.py
│   │   ├── mercadona_investment_strategy.py
│   │   ├── airbnb_purchase_strategy.py
│   │   ├── airbnb_expense_strategy.py
│   │   └── airbnb_investment_strategy.py
│   ├── factories/                 # Fábricas para obtener la estrategia adecuada
│   │   └── accounting_strategy_factory.py
│   ├── dtos/                      # DTO para asientos contables
│   │   └── accounting_entry_dto.py
│   ├── enums/                     # Enumeraciones para cuentas y asientos
│   │   └── accounting_enums.py
│   └── models/                    # Modelo de Asiento Contable
│       └── accounting_entry.py
│
├── notifications/                # Escenario 3: Notificaciones (Observer)
│   ├── controllers/               # Controladores para notificaciones
│   │   └── notification_controller.py
│   ├── observers/                 # Observadores (Observer Pattern)
│   │   ├── base_observer.py
│   │   ├── user_notification_observer.py
│   │   ├── accounting_observer.py
│   │   └── balance_observer.py
│   ├── services/                  # Servicio de notificaciones
│   │   └── notification_service.py
│   ├── dtos/                      # DTOs para notificaciones
│   │   └── notification_dto.py
│   └── enums/                     # Enumeraciones de notificación
│       └── notification_enums.py
│
├── taxes/                         # Escenario 4: Cálculo de Impuestos (Strategy o Chain of Responsibility)
│   ├── controllers/               # Controladores para impuestos
│   │   └── tax_controller.py
│   ├── services/                  # Lógica de impuestos
│   │   └── tax_service.py
│   ├── strategies/                # Estrategias para el cálculo de impuestos
│   │   ├── base_tax.py
│   │   ├── mercadona_tax_strategy.py
│   │   ├── airbnb_tax_strategy.py
│   │   └── special_tax_strategy.py
│   ├── dtos/                      # DTOs para impuestos
│   │   └── tax_dto.py
│   └── enums/                     # Enumeraciones para tipos de impuestos
│       └── tax_type_enum.py
│
├── common/                        # Componentes y utilidades comunes
│   ├── utils/                     # Funciones genéricas (ej. manejo de fechas)
│   │   └── date_utils.py
│   ├── dtos/                      # DTOs comunes
│   │   └── base_response_dto.py
│   └── enums/                     # Enumeraciones generales
│       └── common_enums.py
│
└── config/                        # Configuración del proyecto
    ├── settings.py                # Configuraciones globales
    ├── routes.py                  # Definición de rutas/urls
    └── wsgi.py                    # Configuración WSGI para el despliegue
```

## Uso

- **Panel de Administración:**  
  Accede a `http://127.0.0.1:8000/admin/` (asegúrate de crear un superusuario).

- **Endpoints de la API:**  
  - **Facturas:** `http://127.0.0.1:8000/invoices/`
  - **Contabilidad:** `http://127.0.0.1:8000/accounting/`
  - **Notificaciones:** `http://127.0.0.1:8000/notifications/`
  - **Impuestos:** `http://127.0.0.1:8000/taxes/`
