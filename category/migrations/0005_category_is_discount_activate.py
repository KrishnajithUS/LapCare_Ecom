# Generated by Django 4.1.1 on 2022-10-03 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_category_discount_alter_category_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_discount_activate',
            field=models.BooleanField(default=False),
        ),
    ]