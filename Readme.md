# InvoiceSystem

**InvoiceSystem** is a billing system developed with **Django**.  
It follows a **vertical architecture** and implements several **design patterns**:  
Strategy, Factory, State, Observer, and Chain of Responsibility.

The system manages:

- **Accounting entries generation**: (invoice types: purchases, expenses, investments).
- **Invoice states**: (draft, published, paid, canceled).
- **Notifications**: (Observer / Pub-Sub).
- **Tax calculations**: (Strategy or Chain of Responsibility).

Designed for companies like **Mercadona** and **Airbnb**,  
the system allows business rules customization.

## Features

- **Vertical Architecture**: Code is organized by functionalities:  
  `invoices`, `accounting`, `notifications`, `taxes`, and `common`.
- **Design Patterns**:
  - **Strategy + Factory**: For generating accounting entries.
  - **State**: For managing the invoice lifecycle.
  - **Observer**: For handling important event notifications.
  - **Strategy / Chain of Responsibility**: For tax calculations.
- **Modularity and Scalability**:  
  Easy integration of new functionalities.

## Requirements

- Python 3.8 or higher
- MySQL
- `requirements.txt`

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/victor90braz/invoice-system-patterns-design-vertical-architecture.git
cd InvoiceSystem
```

### 2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
```

### 3. Run the `setup-windows.bat` script (Windows only):

```bash
./setup-windows.bat
```

### 4. Environment configuration:

Create a `.env` file in the project root and add the following environment variables:

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

### 5. Install dependencies:

```bash
pip install -r requirements.txt
pip install mysqlclient
```

### 6. Create a MySQL database:

Access MySQL and create the database:

```bash
mysql -u root -p
CREATE DATABASE InvoiceSystem;
```

### 7. Run migrations:

Ensure that your **`settings.py`** contains the following configuration:

```python
MIGRATION_MODULES = {
    'invoices': 'InvoiceSystem.database.migrations',
}
```

Then, run the following commands to apply the migrations:

```bash
python manage.py makemigrations invoice_app --empty --name initial
python manage.py makemigrations
python manage.py migrate
```

### 8. Insert sample data:

Open the Django shell:

```bash
python manage.py shell
```

Then execute the following commands to insert sample data:

```python
from invoice_app.models import Supplier, Invoice, TaxPolicy

tax_policy = TaxPolicy.objects.create(
    product_type="electronics",
    country="Spain",
    tax_regime="General",
    tax_rate=21.00
)

supplier = Supplier.objects.create(
    name="Tech Supplier",
    email="supplier@example.com",
    tax_policy=tax_policy
)

invoice = Invoice.objects.create(
    invoice_number="INV-001",
    total_value=500.00,
    invoice_type="purchase_invoice",
    supplier=supplier
)

print("✅ Data inserted successfully!")
exit()
```

### 9. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

### 10. Start the development server:

```bash
python manage.py runserver
```

### 11. Run unit tests:

```bash
python manage.py test invoice_app.tests
python manage.py test invoice_app.tests.unit.notifications.test_notifications.InvoiceNotificationTest
```

### 12. Generate Test Coverage Report in HTML:

Install the `coverage` package if it's not already installed:

```bash
pip install coverage
```

Run the tests with coverage:

```bash
coverage run manage.py test invoice_app.tests
coverage report
coverage html
```