from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_kg', 'quantity_in_stock')
    list_editable = ('price_per_kg', 'quantity_in_stock')
