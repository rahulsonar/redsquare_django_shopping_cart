# Generated by Django 2.1 on 2018-11-02 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, limit_choices_to={'parent': None}, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
