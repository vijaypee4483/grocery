# Generated by Django 3.2.12 on 2022-07-01 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220701_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 1, 17, 19, 53, 774287)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 1, 17, 19, 53, 774263)),
        ),
    ]
