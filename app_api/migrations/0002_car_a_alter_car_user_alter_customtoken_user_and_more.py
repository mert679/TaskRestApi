# Generated by Django 4.0.3 on 2024-04-08 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='a',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customtoken',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='car',
            table='car',
        ),
    ]
