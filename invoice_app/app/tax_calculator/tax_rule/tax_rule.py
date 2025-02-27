class TaxRule:
    def __init__(self, country=None, product_type=None, tax_regime=None, strategy=None):
        self.country = country
        self.product_type = product_type
        self.tax_regime = tax_regime
        self.strategy = strategy

    def applies_to(self, invoice):
        return (
            (self.country is None or self.country == invoice.supplier.country) and
            (self.product_type is None or self.product_type == invoice.product_type) and
            (self.tax_regime is None or self.tax_regime == invoice.tax_regime)
        )
