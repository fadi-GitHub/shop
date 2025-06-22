from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.DecimalField(max_digits=10, decimal_places=2)
    
    def is_available(self, requested_quantity):
        return self.quantity_in_stock > 0 and self.quantity_in_stock >= requested_quantity
    
    def reduce_stock(self, quantity):
        self.quantity_in_stock -= quantity
        self.save()
    
    def get_stock_message(self, requested_quantity):
        if self.quantity_in_stock == 0:
            return f"Sorry, {self.name} is out of stock."
        elif self.quantity_in_stock < requested_quantity:
            return f"Sorry, we only have {self.quantity_in_stock}kg of {self.name} available."
        return None
