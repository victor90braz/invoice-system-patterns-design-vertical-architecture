from django.test import TestCase
from decimal import Decimal

import factory
from invoice_app.app.tax_calculator.service.tax_calculator import TaxCalculator
from invoice_app.database.factories.invoice_factory import InvoiceFactory
from invoice_app.database.factories.supplier_factory import SupplierFactory
from invoice_app.database.factories.tax_policy_factory import TaxPolicyFactory

class TestTaxCalculator(TestCase):
    def test_calculate_total_tax_with_matching_policy(self):
        # Arrange: Crear una política de impuestos
        tax_policy = TaxPolicyFactory.create(rate=Decimal("21.00"), product_type="electronics")

        # Crear un proveedor
        supplier = SupplierFactory.create()
        supplier.tax_policies.set([tax_policy])  # ✅ Asignamos tax_policies correctamente

        # Crear una factura de tipo "electronics"
        invoice = InvoiceFactory.create(
            total_value=Decimal("100.00"),
            invoice_type="electronics",
            supplier=supplier
        )

        # Act: Calcular impuestos
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 1)  # ✅ Validamos que el proveedor tiene 1 política
        self.assertEqual(total_tax, Decimal("21.00"))  # ✅ (100 * 0.21 = 21)

    def test_calculate_total_tax_with_multiple_policies(self):
        # Arrange: Crear múltiples políticas de impuestos con valores correctos
        tax_policies = TaxPolicyFactory.create_batch(
            2, 
            rate=factory.Iterator([Decimal("21.00"), Decimal("10.00")]),  # ✅ Asignamos tasas diferentes
            product_type="electronics", 
            tax_regime="freelancer"
        )

        # Crear un proveedor
        supplier = SupplierFactory.create()
        supplier.tax_policies.set(tax_policies)  # ✅ Asignamos tax_policies correctamente

        # Crear una factura de tipo "electronics"
        invoice = InvoiceFactory.create(
            total_value=Decimal("200.00"),
            invoice_type="electronics",
            supplier=supplier
        )

        # Act: Calcular impuestos
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 2)  # ✅ Validamos que tiene 2 políticas
        self.assertEqual(total_tax, Decimal("62.00"))  # ✅ (200 * 0.21 + 200 * 0.10 = 62)

    def test_calculate_total_tax_no_matching_policy(self):
        # Arrange: Crear un proveedor sin políticas de impuestos
        supplier = SupplierFactory.create()
        supplier.tax_policies.clear()  # ✅ Aseguramos que no tenga políticas asignadas

        # Crear una factura con tipo de producto sin políticas
        invoice = InvoiceFactory.create(
            total_value=Decimal("150.00"),
            invoice_type="clothing",  # ✅ No hay política de impuestos para "clothing"
            supplier=supplier
        )

        # Act: Calcular impuestos
        total_tax = TaxCalculator.calculate_total_tax(invoice)

        # Assert
        self.assertEqual(supplier.tax_policies.count(), 0)  # ✅ Validamos que no tiene tax policies
        self.assertEqual(total_tax, Decimal("0.00"))  # ✅ Si no hay políticas, el impuesto debe ser 0
