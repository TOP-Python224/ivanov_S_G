# Generated by Django 4.1.7 on 2023-04-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_rename_published_basket_created_at_basket_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]