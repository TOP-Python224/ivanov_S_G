# Generated by Django 4.1.7 on 2023-04-15 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_basket_products_basket_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='products',
        ),
        migrations.DeleteModel(
            name='Product_cart',
        ),
    ]