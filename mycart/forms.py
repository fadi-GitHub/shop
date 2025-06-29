from django import forms

class CartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        products = kwargs.pop('products')
        super().__init__(*args, **kwargs)
        default_quantities = {
            'Onions': 1,
            'Potatoes': 2,
            'Carros': 1,
        }
        for product in products:
            field_name = f"product_{product.id}" # Unique field name for each product
            self.fields[field_name] = forms.DecimalField(
                label=product.name,
                min_value=0,
                decimal_places=2,
                required=False,
                initial=default_quantities.get(product.name, 1),
                widget=forms.NumberInput(attrs={
                    'class': 'quantity-input w-20 text-right border rounded p-1',
                    'id': f'quantity-{product.id}',
                    'step': '0.5',
                    'min': '0',
                    'data-price': str(product.price_per_kg),
                    'placeholder': f'Qty for {product.name}',
                    'autocomplete': 'off',
                })
            )
