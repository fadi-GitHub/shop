from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
            preserve_default=False,
        ),
    ]
