# Generated by Django 4.1.7 on 2023-04-15 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_basket_options_basket_published_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='quantity',
            new_name='total_price',
        ),
    ]