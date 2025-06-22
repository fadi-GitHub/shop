from django.core.management.base import BaseCommand
from mycart.models import Product

class Command(BaseCommand):
    help = 'Load or update dummy products into the Product table'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        products = [
            Product(name='Onions', price_per_kg=2, quantity_in_stock=100),
            Product(name='Potatoes', price_per_kg=5, quantity_in_stock=200),
            Product(name='Carrots', price_per_kg=4, quantity_in_stock=150),
        ]

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('Dummy products loaded successfully.'))
