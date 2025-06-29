from django.db import migrations

def calculate_total_price(apps, schema_editor):
    PurchaseItem = apps.get_model('mycart', 'PurchaseItem')
    for item in PurchaseItem.objects.all():
        item.total_price = item.quantity * item.product.price_per_kg
        item.save()

def reverse_calculate_total_price(apps, schema_editor):
    PurchaseItem = apps.get_model('mycart', 'PurchaseItem')
    for item in PurchaseItem.objects.all():
        item.total_price = 0
        item.save()

class Migration(migrations.Migration):
    dependencies = [
        ('mycart', '0003_purchaseitem_total_price'), 
    ]

    operations = [
        migrations.RunPython(calculate_total_price, reverse_code=reverse_calculate_total_price),
    ]