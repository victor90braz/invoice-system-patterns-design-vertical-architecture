```markdown
# InvoiceSystem

**InvoiceSystem** es un sistema desarrollado con **Django**.  
Implementa una **arquitectura vertical** y usa varios **patrones de diseño**:  
Estrategia, Fábrica, Estado, Observador y Cadena de Responsabilidad.

El sistema gestiona:

- **Generación de asientos contables**: (tipos de factura: compras, gastos, inversiones).
- **Estados de facturas**: (borrador, publicado, pagado, cancelado).
- **Notificaciones**: (Observador / Pub-Sub).
- **Cálculo de impuestos**: (Estrategia o Cadena de Responsabilidad).

Diseñado para empresas como **Mercadona** y **Airbnb**,  
el sistema permite personalizar reglas de negocio.

## Características

- **Arquitectura Vertical**: Organización del código por funcionalidades:  
  `invoices`, `accounting`, `notifications`, `taxes` y `common`.
- **Patrones de Diseño**:
  - **Estrategia + Fábrica**: Para generar asientos contables.
  - **Estado**: Para gestionar el ciclo de vida de las facturas.
  - **Observador**: Para manejar notificaciones de eventos importantes.
  - **Estrategia / Cadena de Responsabilidad**: Para cálculos de impuestos.
- **Modularidad y Escalabilidad**:  
  Fácil integración de nuevas funcionalidades.

## Requisitos

- requirements.txt

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/victor90braz/invoice-system-patterns-design-vertical-architecture.git
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

3. **Ejecutar el script `setup-windows.bat` (solo en Windows):**
   ```bash
   ./setup-windows.bat
   ```

5. **Ejecutar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear un superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

```plaintext
InvoiceSystem/
│
├── invoices/                      # Facturas (Patrón Estado)
│   ├── controllers/               # Controladores de facturas
│   ├── models/                    # Modelo de factura
│   ├── states/                    # Implementación del patrón Estado
│   ├── services/                  # Lógica de negocio de facturas
│   ├── dtos/                      # DTOs de facturas
│   ├── enums/                     # Enums de estados
│   └── utils/                     # Utilidades y validaciones
│
├── accounting/                    # Asientos contables (Estrategia + Fábrica)
│   ├── controllers/               # Controladores contables
│   ├── services/                  # Lógica de negocio de asientos
│   ├── strategies/                # Estrategias contables
│   │   ├── mercadona_purchase_strategy.py  # Estrategia de compras Mercadona
│   │   ├── mercadona_expense_strategy.py    # Estrategia de gastos Mercadona
│   │   ├── mercadona_investment_strategy.py # Estrategia de inversiones Mercadona
│   │   ├── airbnb_purchase_strategy.py     # Estrategia de compras Airbnb
│   │   ├── airbnb_expense_strategy.py      # Estrategia de gastos Airbnb
│   │   └── airbnb_investment_strategy.py  # Estrategia de inversiones Airbnb
│   ├── factories/                 # Fábricas de estrategias contables
│   ├── dtos/                      # DTOs de asientos contables
│   ├── enums/                     # Enums contables
│   └── models/                    # Modelo de asiento contable
│
├── notifications/                # Notificaciones (Patrón Observador)
│   ├── controllers/               # Controladores de notificaciones
│   ├── observers/                 # Observadores
│   ├── services/                  # Servicio de notificaciones
│   ├── dtos/                      # DTOs de notificaciones
│   └── enums/                     # Enums de notificaciones
│
├── taxes/                         # Cálculo de impuestos (Estrategia o Cadena de Responsabilidad)
│   ├── controllers/               # Controladores de impuestos
│   ├── services/                  # Lógica de impuestos
│   ├── strategies/                # Estrategias de impuestos
│   │   ├── mercadona_tax_strategy.py  # Estrategia de impuestos Mercadona
│   │   ├── airbnb_tax_strategy.py     # Estrategia de impuestos Airbnb
│   │   └── special_tax_strategy.py   # Estrategia de impuestos especial
│   ├── dtos/                      # DTOs de impuestos
│   └── enums/                     # Enums de impuestos
│
├── common/                        # Componentes comunes
│   ├── utils/                     # Funciones generales (ej. manejo de fechas)
│   ├── dtos/                      # DTOs comunes
│   └── enums/                     # Enums generales
│
└── config/                        # Configuración del proyecto
    ├── settings.py                # Ajustes globales
    ├── routes.py                  # Definiciones de rutas
    └── wsgi.py                    # Configuración WSGI para despliegue
```

## Uso

- **Panel de administración:**  
  Accede en `http://127.0.0.1:8000/admin/` (debes crear un superusuario).

- **Puntos finales API:**  
  - **Facturas:** `http://127.0.0.1:8000/invoices/`
  - **Contabilidad:** `http://127.0.0.1:8000/accounting/`
  - **Notificaciones:** `http://127.0.0.1:8000/notifications/`
  - **Impuestos:** `http://127.0.0.1:8000/taxes/`
```

