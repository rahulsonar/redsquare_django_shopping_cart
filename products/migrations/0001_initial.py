# Generated by Django 2.1 on 2018-10-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=300)),
                ('product_price', models.FloatField()),
                ('product_status', models.DecimalField(decimal_places=0, max_digits=2)),
                ('date_added', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]