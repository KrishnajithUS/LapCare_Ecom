# Generated by Django 4.1.1 on 2022-10-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_remove_products_offer_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='offer_product',
            field=models.FloatField(blank=True, default=0),
        ),
    ]