# Generated by Django 3.2.12 on 2022-06-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]