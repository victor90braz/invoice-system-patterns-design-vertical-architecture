```markdown
# InvoiceSystem

**InvoiceSystem** es un sistema de facturación desarrollado con **Django**.  
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
  `invoices`, `accounting`, `notifications`, `taxes`, y `common`.
- **Patrones de Diseño**:
  - **Estrategia + Fábrica**: Para generar asientos contables.
  - **Estado**: Para gestionar el ciclo de vida de las facturas.
  - **Observador**: Para manejar notificaciones de eventos importantes.
  - **Estrategia / Cadena de Responsabilidad**: Para cálculos de impuestos.
- **Modularidad y Escalabilidad**:  
  Fácil integración de nuevas funcionalidades.

## Requisitos

- Python 3.8 o superior
- MySQL
- `requirements.txt`

## Instalación

### 1. Clonar el repositorio:

```bash
git clone https://github.com/victor90braz/invoice-system-patterns-design-vertical-architecture.git
cd InvoiceSystem
```

### 2. Crear y activar un entorno virtual:

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Ejecutar el script `setup-windows.bat` (solo en Windows):

```bash
./setup-windows.bat
```

### 4. Configuración de entorno:

Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes variables de entorno:

```env
DB_NAME=invoice_system_db
DB_USER=root
DB_PASSWORD=root
DB_HOST=127.0.0.1
DB_PORT=3306
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 6. Instalar dependencias:

```bash
pip install -r requirements.txt
pip install mysqlclient
```

### 7. Crear base de datos en MySQL:

Accede a MySQL y crea la base de datos:

```bash
mysql -u root -p
CREATE DATABASE InvoiceSystem;
```

### 8. Ejecutar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Crear un superusuario (opcional):

```bash
python manage.py createsuperuser
```

### 10. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

### 11. Ejecutar testings

```bash
python manage.py test InvoiceSystem.tests.unit.accounting.test_accounting_strategies
```
