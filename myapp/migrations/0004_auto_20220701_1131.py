# Generated by Django 3.2.12 on 2022-07-01 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_orders_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]