# Generated by Django 5.0.2 on 2024-02-17 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_personamodel_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='personamodel',
            name='idtipoVehiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.tipovehiculo'),
        ),
    ]
