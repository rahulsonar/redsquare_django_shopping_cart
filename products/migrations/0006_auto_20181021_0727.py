# Generated by Django 2.1 on 2018-10-21 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productattributes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productattributes',
            old_name='product_id',
            new_name='product',
        ),
    ]
