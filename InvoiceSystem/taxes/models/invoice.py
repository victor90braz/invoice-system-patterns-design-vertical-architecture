from django.db import models

class Invoice(models.Model):
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100)  # País proveedor
    product_type = models.CharField(max_length=100)  # Tipo de producto/servicio
    tax_regime = models.CharField(max_length=100)  # Régimen fiscal (Ej. 'general', 'reducido', etc.)

    def is_international(self):
        return self.country != "España"

    def is_reduced_rate(self):
        return self.product_type in ["food", "medicine"]

    def is_simplified_regime(self):
        return self.tax_regime == "simplified"
