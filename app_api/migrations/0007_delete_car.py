# Generated by Django 4.0.3 on 2024-04-09 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0006_alter_car_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
    ]
